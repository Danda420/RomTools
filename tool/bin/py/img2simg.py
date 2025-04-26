from __future__ import print_function, division
from sys import stderr, stdout
from functools import partial
from binascii import unhexlify
from os import fstat
import stat
import argparse
from enum import IntEnum
from struct import pack, unpack, calcsize
from os import SEEK_CUR, SEEK_END, SEEK_SET


class SparseChunkType(IntEnum):
    RAW = 0xCAC1
    FILL = 0xCAC2
    DONT_CARE = 0xCAC3
    CRC32 = 0xCAC4


class SimgWriter(object):
    file_header = "<I4H4I"
    chunk_header = "<2H2I"
    file_header_size = calcsize(file_header)
    chunk_header_size = calcsize(chunk_header)

    def __init__(self, outf, start_block_offset=0, end_block_offset=None, blocksize=4096, debug=0, dont_care=()):
        assert blocksize > 0
        assert blocksize % 4 == 0

        self.outf = outf
        self.start_block_offset = start_block_offset
        self.end_block_offset = end_block_offset
        self.blocksize = blocksize
        self.debug = debug
        self.dont_care = dont_care

        self.nchunks = 0  # number of chunks written
        self.nblocks = 0  # number of blocks of data added
        self.npadblocks = 0  # number of DONT_CARE blocks added

        self.ctype = None  # SparseChunkType of current chunk
        self.cval = None  # fill or CRC32 value for current chunk
        self.csize = 0  # number of blocks in current chunk
        self.buf = b''

        # leave room for file header, and write (optional) leading DONT_CARE blocks
        self.outf.write(b'\0' * self.file_header_size)
        self._add_pad_blocks(self.start_block_offset)

    def __enter__(self):
        self.outf.__enter__()
        return self

    def __exit__(self, type, value, traceback):
        self.close()
        self.outf.__exit__(type, value, traceback)
        return None

    def tell(self):
        return self.outf.tell()

    def flush(self):
        self._close_chunk()

    def _print_state(self, pfx, debug):
        if self.debug >= debug:
            print("%snchunks=%d, nblocks=%d, npadblocks=%d, ctype=%s, cval=%r, csize=%d, len(buf)=%d, tell()=%d" %
                  (pfx, self.nchunks, self.nblocks, self.npadblocks, self.ctype and self.ctype.name, self.cval,
                   self.csize, len(self.buf), self.tell()),
                  file=stderr)

    def close(self):
        if self.buf:
            raise RuntimeError(
                '%d leftover bytes (data written must be a multiple of blocksize %d)' % (len(self.buf), self.blocksize))

        # write final unwritten chunk and (optional) trailing DONT_CARE chunk
        self._close_chunk()
        if self.end_block_offset != None:
            self._add_pad_blocks(self.end_block_offset - self.nblocks)
            self._close_chunk()

        self.outf.seek(0, SEEK_SET)
        self._print_state('  writing final header: ', 1)
        self.outf.write(pack(self.file_header,
                             0xED26FF3A,  # magic
                             1, 0,  # version 1.0
                             self.file_header_size, self.chunk_header_size, self.blocksize, self.nblocks, self.nchunks,
                             0  # checksum
                             ))
        self.outf.seek(0, SEEK_END)

    def _close_chunk(self):
        self._print_state('   top of _close_chunk: ', 1)

        if self.csize == 0:
            return

        if self.ctype == SparseChunkType.RAW:
            databytes = self.csize * self.blocksize
            self.outf.seek(- databytes - self.chunk_header_size, SEEK_CUR)  # return to where chunk header belongs
        elif self.ctype == SparseChunkType.DONT_CARE:
            databytes = 0
        else:
            databytes = len(self.cval)

        self.outf.write(pack(self.chunk_header, self.ctype, 0, self.csize, self.chunk_header_size + databytes))

        if self.ctype == SparseChunkType.RAW:
            self.outf.seek(0, SEEK_END)  # go back to end of file
        elif self.ctype == SparseChunkType.DONT_CARE:
            pass
        else:
            self.outf.write(self.cval)

        self.csize = 0
        self.nchunks += 1

        self._print_state('bottom of _close_chunk: ', 1)

    def _add_pad_blocks(self, n=1):
        self._print_state('top of _add_pad_blocks: ', 2)

        if self.buf:
            raise RuntimeError(
                '%d leftover bytes (data written must be a multiple of blocksize %d)' % (len(self.buf), self.blocksize))
        if n <= 0:
            return

        if self.ctype != SparseChunkType.DONT_CARE:
            self._close_chunk()

        self.ctype = SparseChunkType.DONT_CARE
        self.cval = None
        self.csize += n
        self.nblocks += n
        self.npadblocks += n

        self._print_state('bottom _add_pad_blocks: ', 2)

    def _add_data_block(self):
        self._print_state('   top of _add_data_block: ', 2)

        block, self.buf = self.buf, b''
        assert len(block) == self.blocksize

        # determine correct chunk type
        cval = block[:4]
        if block == cval * (self.blocksize // 4):
            if cval in self.dont_care:
                ctype = SparseChunkType.DONT_CARE
                cval = None
            else:
                ctype = SparseChunkType.FILL
        else:
            ctype = SparseChunkType.RAW
            cval = None

        # if chunk type is changing, close out the current chunk
        if self.ctype != ctype or self.cval != cval:
            self._close_chunk()

        # write data for raw chunks immediately, leaving room for chunk header if we just changed
        if ctype == SparseChunkType.RAW:
            if ctype != self.ctype:
                self.outf.write(b'\0' * self.chunk_header_size)
            self.outf.write(block)

        self.ctype = ctype
        self.cval = cval
        self.csize += 1
        self.nblocks += 1

        self._print_state('bottom of _add_data_block: ', 2)

    def write(self, data):
        nblocks = pp = 0

        if self.buf:
            pp = self.blocksize - len(self.buf)
            self.buf += data[:pp]
            if len(self.buf) == self.blocksize:
                self._add_data_block()
                nblocks += 1

        for pp in range(pp, len(data), self.blocksize):
            self.buf = data[pp: pp + self.blocksize]
            if len(self.buf) == self.blocksize:
                self._add_data_block()
                nblocks += 1

        return nblocks


def power_of_2(val):
    num = int(val)
    if num < 256 or (num & (num - 1)):
        raise ValueError
    return num


def hex_pattern(val):
    val = unhexlify(val)
    if len(val) not in (1, 2, 4):
        raise ValueError
    return val * (4 // len(val))


def parse_args(args=None):
    p = argparse.ArgumentParser()
    p.add_argument('img', type=argparse.FileType('rb'))
    p.add_argument('-b', '--blocksize', default=4096, type=power_of_2, help='Sparse block size (default %(default)s)')
    p.add_argument('-o', '--output', default=stdout, metavar='PATH', help='Output file (default is standard output)')
    p.add_argument('-S', '--split', default=None, type=int, metavar='MiB',
                   help='Split output into multiple sparse images of no more than the specified size in MiB (= 2**20 bytes)')
    p.add_argument('-D', '--dont-care', default=[], action='append', type=hex_pattern, metavar='PATTERN',
                   help='Hex pattern (e.g. FFFFFFFF) to treat as DONT_CARE; may be specified multiple times')
    p.add_argument('-d', '--debug', action='count', default=0)
    args = p.parse_args()

    if args.split and not isinstance(args.output, str):
        p.error('Must specify output filename prefix with --output to write split sparse images')

    return p, args


def main():
    p, args = parse_args()

    st = fstat(args.img.fileno())
    if stat.S_ISREG(st.st_mode):
        if st.st_size % args.blocksize != 0:
            p.error('Image size is not an exact multiple of --blocksize %d' % args.blocksize)
        img_total_blocks = st.st_size // args.blocksize
    else:
        img_total_blocks = None
        print(
            'WARNING: Image is not a regular file; cannot verify that it is an exact multiple of --blocksize %d' % args.blocksize,
            file=stderr)
        if args.split:
            print('         Cannot pad split files with DONT_CARE blocks to total block size.', file=stderr)

    start_block = split_number = 0
    done = False

    while not done:
        if args.split:
            outf = open(args.output + '.%d' % split_number, 'wb')
        elif isinstance(args.output, str):
            outf = open(args.output, 'wb')
        else:
            outf = args.output

        with SimgWriter(outf, blocksize=args.blocksize, debug=args.debug, start_block_offset=start_block,
                        end_block_offset=img_total_blocks, dont_care=args.dont_care) as wr:
            for nb, block in enumerate(iter(partial(args.img.read, args.blocksize), b'')):
                wr.write(block)

                if args.split and ((wr.tell() + args.blocksize) >> 20) >= args.split:
                    # writing one more block (might) exceed desired split size in MiB...
                    break
            else:
                # we only reach this when we run out of input "naturally"...
                done = True

            wr.flush()
            print('%s: Wrote %d blocks in %d sparse chunks (%d%% compression)' % (
            outf.name, nb, wr.nchunks, (wr.tell() / (nb * args.blocksize)) * 100), file=stderr)

            start_block += nb
            split_number += 1


if __name__ == '__main__':
    main()