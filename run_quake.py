#!/usr/bin/env python
# coding=utf-8
import os
import sys

exe = '/Developer/Marmalade/5.1/s3e/bin/s3e'
if os.name == 'nt':
    exe += '.bat'

cmd = list(sys.argv)
cmd[0] = exe

cmd.append('-via:"/Volumes/HDD/proger/dev/ciklum/training/client-files/quake-port/build_quake_scons_x86/quake_debug.via"')
os.execvp(cmd[0], cmd)
