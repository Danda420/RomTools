# CLI ROM Tools
## ROM Tool written in bash
To start the tool just open terminal on RomTools folder, then run
```` shell
bash start
# or
./start
````
Same goes for AndroidBootEditor... Just open terminal on AndroidBootEditor folder, then run the command above.
Put boot images that you want to modify on AndroidBootEditor folder.

After starting the tool for the first time, you can just type `romtools` in terminal to start it. for AndroidBootEditor, you can run it with just `booteditor` after running it for the first time 

Before using this tool for the first time, make sure to install proprietary packages..
You can do it by starting the tool first then choose "Install proprietary packages".

***
### Features ###
- Unpack and repack super, ext4, erofs, boot and others.
- Converting images
  - sparse to raw & raw to sparse
  - erofs to ext4
  - raw to dat.br & dat.br to raw
  - and so on...
- Auto generate missing fs_config (file perms depends on the location)
- Mount and umount images
- Custom Scripts (put your scripts into scripts/custom_scripts)
- Zstd unpacking and repacking
***
### Available on ###
- Linux (x86_64)
- Windows WSL (Some features might not work on windows)
***
