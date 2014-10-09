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
print '------------------------------------------------------------------'
reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')

sub_key = _winreg.EnumKey(reg, 1)
n = 2
try:
    while sub_key: # or try
        reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
        sub_key = _winreg.EnumKey(reg, n)
        mess = '|| ' +sub_key+ ' : '
        sys.stdout.write(mess)
        sub_key = '\\'+sub_key
        #print sub_key
        path = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'+sub_key
        #print path
        reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, path)
        ## DisplayVersion
        #key = ('', '', '')
        try:
            key = _winreg.EnumValue(reg, 0)
        except:
            print 'err -<'
            n+=1
            continue
        k = 1
        try:
            while key[0] != 'DisplayVersion':
                key = _winreg.EnumValue(reg, k)
                #print key[0]
                k += 1
            sys.stdout.write(key[1])
            print '\n------------------------------------------------------------------'
        except:
            print 'empty -('
            print '------------------------------------------------------------------'
        n += 1
except:
    print '\n[= end of reg =]'

raw_input('Enter to end...')