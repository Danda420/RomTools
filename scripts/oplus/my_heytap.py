#!/usr/bin/env python
import sys
import shutil
import tempfile

tmp=tempfile.mkstemp()

with open(sys.argv[1]) as fd1, open(tmp[1],'w') as fd2:
    for line in fd1:
        line = line.replace('my_heytap/','system/my_heytap/')
        fd2.write(line)

shutil.move(tmp[1],sys.argv[1])
