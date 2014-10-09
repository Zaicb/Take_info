# -*- coding: utf-8 -*-
#        _   _        __   __
#     /_\ | |__ _ _ \ \ / /_ _ _ _ __ _ ___
#    / _ \| / _` | ' \ V / _` | '_/ _` / _ \
#   /_/ \_\_\__,_|_||_\_/\__,_|_| \__, \___/
#                                 |___/
#
# take info by _winreg from Uninstall
# List of installed programs on PC

import sys
import _winreg

print '------------------------------------------------------------------'
reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')

sub_key = _winreg.EnumKey(reg, 1)
n = 2
try:
    while sub_key:
        reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
        sub_key = _winreg.EnumKey(reg, n)
        mess = '|| ' + sub_key + ' : '
        sys.stdout.write(mess)
        sub_key = '\\'+sub_key
        path = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'+sub_key
        reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, path)
        try:
            key = _winreg.EnumValue(reg, 0)
        except:
            print 'err -<'
            n += 1
            continue
        k = 1
        try:
            while key[0] != 'DisplayVersion':
                key = _winreg.EnumValue(reg, k)
                #print key[0]
                k += 1
            sys.stdout.write(key[1])
            print ''
        except:
            print 'empty -('
        n += 1
except:
    print '\n[= end of reg =]'

raw_input('\nEnter to end...')