# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

# Written by devast8a <devast8a[at]whitefirex.com>
__module_name__ = "Force Part"
__module_version__ = "0.1"
__module_description__ = "Actually part when using ZNC & partdetach2"

from xchat import *
hook = None

def fpart2(userdata):
    global hook
    find_context(None, "*status").command("close")
    unhook(hook)

def fpart(word, word_eol, userdata):
    global hook
    context = get_context()
    ch = context.get_info("channel")
    command("msg *status unloadmod partdetach2")
    command("part " + ch)
    command("msg *status loadmod partdetach2")
    command("close")
    hook = hook_timer(1000, fpart2)

hook_command("fpart", fpart)

def fpart_unload(userdata):
    print("(Force Part)\tUnloaded!")
    
hook_unload(fpart_unload)
print("(Force Part)\tLoaded!")