# CLI ROM Tools for Linux
### Setup ###
1. Clone this repository or download code zip then extract (where you cloned or extracted this tool will detemine the tool directory after you're done setting up)
2. Open terminal on RomTools folder
3. Run this on terminal
```` shell
bash start
# or
./start
````
4. Choose "Install proprietary packages" option (it will auto detect your linux distribution base)

After setting up, you can just type `romtools` in terminal to start it.

***
### Workspace & Usage ###
- The tool uses a Project System. Upon starting, you will be prompted to create a new project or open an existing one.
- Put the files you want to unpack or modify into the input folder.
- Repacked output files are generated in the output folder.
- Decompiled partitions are extracted to your specific project directory located at ROM_WORKDIR/<project_name>

***
### Features ###
- Project Management: Create, switch, and delete isolated workspaces for different ROMs.
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
### System compatibility ###
- Linux x86_64 (distributions based on Arch, Debian, RedHat, and OpenSUSE are supported)
- Windows WSL (features like image mounting and unmounting are unavailable)
***

### Credits ###

[cfig](https://github.com/cfig/Android_boot_image_editor)

[cyberphantom52](https://github.com/cyberphantom52/payload-dumper-rs)

[sekaiacg](https://github.com/sekaiacg/erofs-utils)

[snowwolf725](https://github.com/snowwolf725/Payload_Repack_Tool)

[xpirt-sdat2img](https://github.com/xpirt/sdat2img)

[xpirt-img2sdat](https://github.com/xpirt/img2sdat)

[althafvly-imgextractor](https://github.com/althafvly/AmlogicKitchen/blob/master/bin/imgextractor.py)

[dlenski-PySIMG](https://github.com/dlenski/PySIMG)
