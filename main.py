#      _   _        __   __
#     /_\ | |__ _ _ \ \ / /_ _ _ _ __ _ ___
#    / _ \| / _` | ' \ V / _` | '_/ _` / _ \
#   /_/ \_\_\__,_|_||_\_/\__,_|_| \__, \___/
#                                 |___/

import os
import sys
import _winreg
import win32api

# take info by

reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')

sub_key = _winreg.EnumKey(reg, 1)
n = 2
while sub_key: # or try
    sub_key = _winreg.EnumKey(reg, n)
    print sub_key
    sub_key = '\\'+sub_key
    print sub_key
    path = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'+sub_key
    print path
    reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, path)
    ## DisplayVersion
    #key = ('', '', '')
    key = _winreg.EnumValue(reg, 1)
    k = 1
    try:
        while key[0] != "DisplayVersion":
            key = _winreg.EnumValue(reg, k)
            print key[0]
            k += 1
        print key
    except:
        print 'no keys'
    n += 1