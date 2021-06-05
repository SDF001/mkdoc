#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import zipfile

docs = """usage:
    unzippy zip_file.zip [dest_path]
    It needs at least one arguments.
    zip_file.zip:
        The file needs to be unzipped.
    dest_path:
        The path you want to extract files.It's default value is current path.
    """
if len(sys.argv) == 3:
    zip_file = sys.argv[1]
    dest_path = os.path.join(os.path.abspath('.'), sys.argv[2])
elif len(sys.argv) == 2:
    zip_file = sys.argv[1]
    dest_path = os.path.abspath('.')
else:
    print(docs)
    sys.exit()

print("Processing File " + zip_file)
file=zipfile.ZipFile(zip_file,"r");
for name in file.namelist():
    try:
        utf8name=name.encode('cp437').decode('gbk')
    except:
        utf8name=name.encode('utf-8').decode('utf-8')
    #print("Extracting " + utf8name)
    pathname = os.path.join(dest_path,os.path.dirname(utf8name))
    #print("pathname " + pathname)
    if not os.path.exists(pathname) and pathname!= "":
        os.makedirs(pathname)
    data = file.read(name)
    data=str(data, 'utf-8')
    if not os.path.exists(os.path.join(dest_path,utf8name)):
        fo = open(os.path.join(dest_path,utf8name), "w")
        fo.write(data)
        fo.close
file.close()
print("unzip to %s successfully." % dest_path)
