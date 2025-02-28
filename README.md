# CLI ROM Tools
## Android Kitchen written in bash
To start the tool just open terminal on RomTools folder, then run
```` shell
bash start
# or
./start
````

After starting the tool for the first time, you can just type `romtools` in terminal to start it. 

Before using this tool for the first time, make sure to install proprietary packages..
You can do it by starting the tool first then choose "Install proprietary packages".

***
### Features ###
- Unpack and repack super, ext4, f2fs, erofs, boot images (like boot, vendor boot, etc) and others.
- Converting images
  - sparse to raw & raw to sparse
  - erofs to ext4, erofs to f2fs, ext4 to erofs, ext4 to f2fs, f2fs to ext4, f2fs to erofs
  - raw to dat.br & dat.br to raw
  - and so on...
- Auto generate missing fs_config (file perms depends on the location)
- Mount and umount images
- Custom Scripts (put your scripts into tool/custom_scripts, you can use functions from tool)
- Zstd unpacking and repacking

| Supported Image Types                   |
|-----------------------------------------|
| Android Boot & Vendor boot Image        |
| Android Recovery Image                  |
| Super                                   |
| Ext4                                    |
| F2fs                                    |
| Erofs                                   |
| Payload (unpack)                        |
| Sparsechunk (decompress)                |
***
### Available on ###
- Linux (Arch, Debian, RedHat, OpenSUSE base supported)
- Windows WSL (features like image mounting and unmounting is unavailable)
***

### Credits ###

[cfig](https://github.com/cfig/Android_boot_image_editor)

[cyberphantom52](https://github.com/cyberphantom52/payload-dumper-rs)

[xpirt-sdat2img](https://github.com/xpirt/sdat2img)

[xpirt-img2sdat](https://github.com/xpirt/img2sdat)

[althafvly-imgextractor](https://github.com/althafvly/AmlogicKitchen/blob/master/bin/imgextractor.py)

