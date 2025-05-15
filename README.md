# CLI ROM Tools for Linux
### Setup ###
- Clone this repository or download code zip then extract (where you cloned or extracted this tool will detemine the tool directory after you're done setting up)
- Open terminal on RomTools folder
- Run this on terminal
```` shell
bash start
# or
./start
````
- Choose "Install proprietary packages" option (it will auto detect your linux distribution base)

After setting up, you can just type `romtools` in terminal to start it.

To use the tool, put files you desire to "input" folder, output files are located on "output" folder, while decompiled partitions are extracted to "ROM_WORKDIR" folder inside RomTools folder.

Those folders are auto generated after starting the tool

***
### Features ###
- Unpack and repack super, payload.bin/OTA.zip, ext4, f2fs, erofs, boot images (like boot, vendor boot, etc) and others.
- Converting images
  - sparse to raw & raw to sparse (sparsechunk also supported)
  - erofs to ext4, erofs to f2fs, ext4 to erofs, ext4 to f2fs, f2fs to ext4, f2fs to erofs
  - raw to dat.br & dat.br to raw
  - and so on...
- Auto generate missing fs_config & file_contexts (file perms/context depends on the location)
- Mount and umount images
- Custom Scripts (put your scripts into tool/custom_scripts, you can use functions from tool.. check README.md on tool/custom_scripts/ for functions/scripts/bins usages and desc)
- Zstd compressing and decompressing

| Supported Image Types                   |
|-----------------------------------------|
| Android Boot & Vendor boot Image        |
| Android Recovery Image                  |
| Super                                   |
| Ext4                                    |
| F2fs                                    |
| Erofs                                   |
| Sparsechunk                             |
| Payload                                 |
***
### Available on ###
- Linux x86_64 (Arch, Debian, RedHat, OpenSUSE base supported)
- Windows WSL (features like image mounting and unmounting is unavailable)
***

### Credits ###

[cfig](https://github.com/cfig/Android_boot_image_editor)

[cyberphantom52](https://github.com/cyberphantom52/payload-dumper-rs)

[xpirt-sdat2img](https://github.com/xpirt/sdat2img)

[xpirt-img2sdat](https://github.com/xpirt/img2sdat)

[althafvly-imgextractor](https://github.com/althafvly/AmlogicKitchen/blob/master/bin/imgextractor.py)

[dlenski-PySIMG](https://github.com/dlenski/PySIMG)

[snowwolf725](https://github.com/snowwolf725/Payload_Repack_Tool)
