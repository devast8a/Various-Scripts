#!/usr/bin/python
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

# Written by devast8a <devast8a[at]whitefirex.com>
import httplib
import os
import sys

##################################
## Settings to edit
# Domain where your shit is hosted
domain = "yourdomain.com"

# Path to log.php
path = "path/to/log.php"

# Default values to pass to PHP script
all = "false"
today = "true"

# Use 7zip
use7z = 0
##################################

def process(n):
    if( n[1] == "all" ):
        all = "true"
    if( n[1] == "-et" ):
        today = "false"

if len(sys.argv) > 1:
    process(sys.argv[1])
    
if len(sys.argv) > 2:
    process(sys.argv[2])

print("Connecting to server.")
conn = httplib.HTTPConnection(domain)
conn.request("GET", path+"&all="+all+"&today="+today)
r1 = conn.getresponse()
data = r1.read();

if data == "No files to grab":
    print(data)
    exit(1)
    
f = file("temp.tar.gz", "wb")
f.write(data)
f.close();

if use7z:
    print("!!! Uncompressing.")
    os.spawnl(os.P_WAIT, "7z", "7z", "e", "temp.tar.gz", "-y")
    print("!!! Unpacking.");
    os.spawnl(os.P_WAIT, "7z", "7z", "e", "temp.tar", "-y")
    print("\nObtained new logs!!")
    os.remove("temp.tar.gz")
    os.remove("temp.tar")
else:
    print("!!! Uncompressing.")
    os.spawnl(os.P_WAIT, "gzip", "gzip", "-d", "temp.tar.gz")
    print("!!! Unpacking.");
    os.spawnl(os.P_WAIT, "tar", "tar", "-xf", "temp.tar")
    print("\nObtained new logs!!")
    os.remove("temp.tar")