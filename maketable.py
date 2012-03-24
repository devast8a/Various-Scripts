#!/usr/bin/python
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.
import sys
import random

min = 0;
max = 255;
alignment = "2";

if len(sys.argv) == 2:
    max = int(sys.argv[1])
    
elif len(sys.argv) == 3:
    min = int(sys.argv[1])
    max = int(sys.argv[2])
    
elif len(sys.argv) == 4:
    min = int(sys.argv[1])
    max = int(sys.argv[2])
    alignment = sys.argv[3]
else:
    print( "%s [max]" % (sys.argv[0]) )
    print( "%s [min] [max]" % (sys.argv[0]) )
    print( "%s [min] [max] [align]" % (sys.argv[0]) )
    print( "by devast8a <devast8a[at]whitefirex.com>\n----------------------------------------\n\n" )

format = "0x%0" + alignment + ".X, "

random.seed()

a = []
for x in xrange(min, max+1):
    while 1:
        v = random.randint(min, max)
        if v not in a:
            a.append(v)
            break
    
    sys.stdout.write( format % (v) );
    if x % 8 == 7:
        sys.stdout.write( "\n" );