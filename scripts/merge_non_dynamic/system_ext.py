#!/usr/bin/env python
import sys
import os
import tempfile

tmp=tempfile.mkstemp()

with open(sys.argv[1]) as fd1, open(tmp[1],'w') as fd2:
    for line in fd1:
        line = line.replace('system_ext/','system/system_ext/')
        fd2.write(line)

os.rename(tmp[1],sys.argv[1])
