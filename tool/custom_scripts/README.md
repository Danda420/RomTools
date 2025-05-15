# Function & binaries lists and usages

## Unpack images functions

### unpack_ext4
#### usage: unpack_ext4 [image] (no file extension needed)
unpacks ext4 image and outputs it into ROM_WORKDIR/EXT4

### unpack_erofs
#### usage: unpack_erofs [image] (no file extension needed)
unpacks erofs image and outputs it into ROM_WORKDIR/erofs

### unpack_f2fs
#### usage: unpack_f2fs [image] (no file extension needed)
unpacks f2fs image and outputs it into ROM_WORKDIR/F2FS


***
## Repack images functions

### repack_ext4_cmd
#### usage: repack_ext4_cmd [extracted partition name] [partition size]
compiles extracted ext4 image into raw .img (output img file is in output dir)

### repack_erofs_cmd
#### usage: repack_erofs_cmd [extracted partition name] [erofs compressor,compression level] (for ex: lz4hc,9) [0/1] (legacy kernel: 1, newer kernel: 0)
compiles extracted erofs image into raw .img (output img file is in output dir)

### repack_f2fs_cmd
#### usage: repack_f2fs_cmd [extracted partition name]
compiles extracted ext4 image into raw .img (output img file is in output dir)


***
## FSType conversion functions

### convert_ext4_erofs
#### usage: convert_ext4_erofs [image] (no file extension needed)
converts ext4 image on input dir to erofs (output img file is in output dir)

### convert_ext4_f2fs
#### usage: convert_ext4_f2fs [image] (no file extension needed)
converts ext4 image on input dir to f2fs (output img file is in output dir)

### convert_erofs_ext4
#### usage: convert_erofs_ext4 [image] (no file extension needed)
converts erofs image on input dir to ext4 (output img file is in output dir)

### convert_erofs_f2fs
#### usage: convert_erofs_f2fs [image] (no file extension needed)
converts erofs image on input dir to f2fs (output img file is in output dir)

### convert_f2fs_ext4
#### usage: convert_f2fs_ext4 [image] (no file extension needed)
converts f2fs image on input dir to ext4 (output img file is in output dir)

### convert_f2fs_erofs
#### usage: convert_erofs_f2fs [image] (no file extension needed)
converts f2fs image on input dir to erofs (output img file is in output dir)

### repack_ext4_as_erofs_cmd 
#### usage: repack_ext4_as_erofs_cmd [extracted partition name] [erofs compressor,compression level] (for ex: lz4hc,9) [0/1] (legacy kernel: 1, newer kernel: 0)
compiles an already extracted ext4 image into erofs raw .img (output img file is in output dir)

### repack_ext4_as_f2fs_cmd 
#### usage: repack_ext4_as_f2fs_cmd [extracted partition name]
compiles an already extracted ext4 image into f2fs raw .img (output img file is in output dir)

### repack_erofs_as_ext4_cmd 
#### usage: repack_erofs_as_ext4_cmd [extracted partition name] [partition size]
compiles an already extracted erofs image into ext4 raw .img (output img file is in output dir)

### repack_erofs_as_f2fs_cmd 
#### usage: repack_erofs_as_f2fs_cmd [extracted partition name]
compiles an already extracted erofs image into f2fs raw .img (output img file is in output dir)

### repack_f2fs_as_ext4_cmd 
#### usage: repack_f2fs_as_ext4_cmd [extracted partition name] [partition size]
compiles an already extracted f2fs image into ext4 raw .img (output img file is in output dir)

### repack_f2fs_as_erofs_cmd 
#### usage: repack_ext4_as_erofs_cmd [extracted_partition_name [erofs compressor,compression level] (for ex: lz4hc,9) [0/1] (legacy kernel: 1, newer kernel: 0)
compiles an already extracted f2fs image into erofs raw .img (output img file is in output dir)


***
## OTA stuff

### payload_all
#### usage: payload_all
unpacks all partitions from payload.bin in input dir and outputs the content into output dir

### dump specific partitions from payload.bin
#### usage: $BIN/payload [payload.bin file] -c [number of threads -p [partitions] (for ex: vendor,odm,system,...) -o [output dir] -q

### payload_compile
#### usage: payload_compile
needs confirmation if images in input dir is the partitions you wanna compile into payload.bin.

compiles raw images in input dir into payload.bin (also outputs payload_properties.txt) and outputs it into output dir (check dynamic_partitions.conf file for specific configurations and common_firmware_images file for images that's not included into super)

### payload_compile_ota
#### usage: payload_compile_ota
needs confirmation if images in input dir is the partitions you wanna compile into OTA.zip.

compiles raw images in input dir into OTA.zip and outputs it into output dir (check dynamic_partitions.conf file for specific configurations and common_firmware_images file for images that's not included into super)


### inc_dynamic_compress
#### usage: inc_dynamic_compress 
needs confirmation if images in input dir is the partitions you wanna compress.

autogenerates dynamic_partitions_op_list, updater-script and compresses raw imgs in input dir into .dat.br and outputs it into output dir (check dynamic_partitions.conf file for specific configurations)

### inc_dynamic_decompress
#### usage: inc_dynamic_decompress
decompresses .dat.br files into raw images and outputs it into output dir

### decompress sparsechunk
#### usage: simg2img [sparsechunk pattern] (for ex: imagename is super.img.0-11, then input: super.img.*) [output]
converts sparsechunk into raw image

### compress sparsechunk
#### usage: python $PYSCRIPTS/img2simg.py [raw .img file] -S [chunk size in MiB] -o [output name] (for ex $DIROUT/super.img, it'll convert it into sparsechunks with pattern: super.img.0-X)
converts raw image into sparsechunks

***
## Miscs

### rebuild_ext4
#### usage: rebuild_ext4 [image] (no file extension needed)
rebuilds ext4 image on input dir and outputs it on output dir (this'll be useful if you just wanna remove avb and dont want to modify anything)

### resize_img
#### usage: resize_img [image] (no file extension needed) [smallest/freespace]
if using freespace, set FREESPACE variable before executing this function (for ex: FREESPACE=40, size is in MB).

resizes image file size

### mount_imgs 
#### usage: mount_imgs [options] (for ex: mount_imgs "loop", mount_imgs "o,nosuid,nodev,relatime,uhelper=udisks2,loop")
mounts images located in ROM_WORKDIR to ROM_WORKDIR/image

### patch_merge_fsconf_contexts
#### usage: patch_merge_fsconf_contexts [partition name] [fs_config file] [file_contexts file]
changes "system/$partition" to "$partition" from fs_config and "/system/$partition" to "/$partition for merging fs_config and contexts to system (but probably you still need to do more than those stuff for some oems to merge the partitions)


