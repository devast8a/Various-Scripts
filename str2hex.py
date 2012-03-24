#!/usr/bin/python
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.
import sys

if len(sys.argv) == 1:
    print( "%s [text]\n- by devast8a <devast8a[at]whitefirex.com>" % (sys.argv[0]) )
else:
    i = 0
    for c in ' '.join(sys.argv[1:]):
        sys.stdout.write( "0x%02.X, " % (ord(c)) )
        if i % 8 == 7:
            sys.stdout.write( "\n" )
        i+=1