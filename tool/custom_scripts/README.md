
# Function & Binaries Lists and Usages

---

## Unpack Images Functions

### `unpack_ext4`
Unpacks ext4 image into `ROM_WORKDIR/EXT4`.
```shell
usage: unpack_ext4 [image]  # no file extension needed
```

### `unpack_erofs`
Unpacks EROFS image into `ROM_WORKDIR/erofs`.
```shell
usage: unpack_erofs [image]  # no file extension needed
```

### `unpack_f2fs`
Unpacks F2FS image into `ROM_WORKDIR/F2FS`.
```shell
usage: unpack_f2fs [image]  # no file extension needed
```

---

## Repack Images Functions

### `repack_ext4_cmd`
Compiles extracted ext4 image into a raw `.img` (output img file is in output dir)
```shell
usage: repack_ext4_cmd [extracted partition name] [partition size]
```

### `repack_erofs_cmd`
Compiles extracted EROFS image into a raw `.img` (output img file is in output dir)
```shell
usage: repack_erofs_cmd [extracted partition name] [compressor,level] [0/1]
# Example: repack_erofs_cmd vendor lz4hc,9 1 (legacy kernel: 1, newer kernel: 0)
```

### `repack_f2fs_cmd`
Compiles extracted F2FS image into a raw `.img` (output img file is in output dir)
```shell
usage: repack_f2fs_cmd [extracted partition name]
```

---

## Filesystem Type Conversion Functions

### `convert_ext4_erofs`
Converts ext4 image to EROFS. (input .img should be in input dir, output will be in output dir)
```shell
usage: convert_ext4_erofs [image] # no file extension needed
```

### `convert_ext4_f2fs`
Converts ext4 image to F2FS. (input .img should be in input dir, output will be in output dir)
```shell
usage: convert_ext4_f2fs [image] # no file extension needed
```

### `convert_erofs_ext4`
Converts EROFS image to ext4. (input .img should be in input dir, output will be in output dir)
```shell
usage: convert_erofs_ext4 [image] # no file extension needed
```

### `convert_erofs_f2fs`
Converts EROFS image to F2FS. (input .img should be in input dir, output will be in output dir)
```shell
usage: convert_erofs_f2fs [image] # no file extension needed
```

### `convert_f2fs_ext4`
Converts F2FS image to ext4. (input .img should be in input dir, output will be in output dir)
```shell
usage: convert_f2fs_ext4 [image] # no file extension needed
```

### `convert_f2fs_erofs`
Converts F2FS image to EROFS. (input .img should be in input dir, output will be in output dir)
```shell
usage: convert_f2fs_erofs [image] # no file extension needed
```

### `repack_ext4_as_erofs_cmd`
compiles an already extracted ext4 image into erofs raw .img (output img file is in output dir)
```shell
usage: repack_ext4_as_erofs_cmd [partition name] [compressor,level] [0/1]
# Example: repack_ext4_as_erofs_cmd vendor lz4hc,9 1 (legacy kernel: 1, newer kernel: 0)
```

### `repack_ext4_as_f2fs_cmd`
compiles an already extracted ext4 image into f2fs raw .img (output img file is in output dir)
```shell
usage: repack_ext4_as_f2fs_cmd [partition name]
```

### `repack_erofs_as_ext4_cmd`
compiles an already extracted erofs image into ext4 raw .img (output img file is in output dir)
```shell
usage: repack_erofs_as_ext4_cmd [partition name] [partition size]
```

### `repack_erofs_as_f2fs_cmd`
compiles an already extracted erofs image into f2fs raw .img (output img file is in output dir)
```shell
usage: repack_erofs_as_f2fs_cmd [partition name]
```

### `repack_f2fs_as_ext4_cmd`
compiles an already extracted f2fs image into ext4 raw .img (output img file is in output dir)
```shell
usage: repack_f2fs_as_ext4_cmd [partition name] [partition size]
```

### `repack_f2fs_as_erofs_cmd`
compiles an already extracted f2fs image into erofs raw .img (output img file is in output dir)
```shell
usage: repack_f2fs_as_erofs_cmd [partition name] [compressor,level] [0/1]
# Example: repack_f2fs_as_erofs_cmd vendor lz4hc,9 1 (legacy kernel: 1, newer kernel: 0)
```

---

## OTA-Related Utilities

### `payload_all`
Unpacks all partitions from `payload.bin` in input dir into the output directory.
```shell
usage: payload_all
```

### Dump specific partitions from `payload.bin`
```shell
usage: $BIN/payload [payload.bin] -c [threads] -p [partitions] -o [output dir] -q
```

### `payload_compile`
compiles raw images in `input` dir into `payload.bin` (also outputs `payload_properties.txt`) and outputs it into output dir (check `dynamic_partitions.conf` file for specific configurations and `common_firmware_images` file for images that's not included into super)

needs confirmation if images in input dir is the partitions you wanna compile into payload.bin.
```shell
usage: payload_compile
```

### `payload_compile_ota`
Same as `payload_compile`, but outputs an OTA `.zip`.
```shell
usage: payload_compile_ota
```

### `inc_dynamic_compress`
autogenerates `dynamic_partitions_op_list`, `updater-script` and compresses raw imgs in input dir into `.dat.br` and outputs it into output dir (check `dynamic_partitions.conf` file for specific configurations)

needs confirmation if images in input dir is the partitions you wanna compress.
```shell
usage: inc_dynamic_compress
```

### `inc_dynamic_decompress`
Decompresses `.dat.br` files into raw images.
```shell
usage: inc_dynamic_decompress
```

### Decompress sparsechunk
converts sparsechunk into raw image
```shell
usage: simg2img [pattern] [output]
# Example: simg2img super.img.* $DIROUT/super.img
```

### Compress sparsechunk
converts raw image into sparsechunks
```shell
usage: python $PYSCRIPTS/img2simg.py [img file] -S [chunk size MiB] -o [output name]
# Example: python $PYSCRIPTS/img2simg.py $DIRIN/super.img -S 512 -o $DIROUT/super.img (this will output super.img.0-X)
```

---

## Miscellaneous

### `rebuild_ext4`
Rebuilds ext4 image in input dir. Useful for removing AVB without changes.
```shell
usage: rebuild_ext4 [image]
```

### `resize_img`
```shell
usage: resize_img [image] [smallest|freespace]
# If using freespace, set FREESPACE env var first (e.g., FREESPACE=40) above the resize_img function in MB
# Example:
# FREESPACE=40
# resize_img $DIROUT/system.img freespace
```
Resize image file size.

### `mount_imgs`
Mounts images from `ROM_WORKDIR` to `ROM_WORKDIR/$image`.
```shell
usage: mount_imgs [options]
# Examples: 
# mount_imgs "loop"
# mount_imgs "o,nosuid,nodev,relatime,uhelper=udisks2,loop"
```

### `patch_merge_fsconf_contexts`
changes "system/$partition" to "$partition" from fs_config and "/system/$partition" to "/$partition for merging fs_config and contexts to system (but probably you still need to do more than those stuff for some oems to merge the partitions)
```shell
usage: patch_merge_fsconf_contexts [partition] [fs_config file] [file_contexts file]
# Example: patch_merge_fsconf_contexts system system_fs_config system_file_contexts
```
