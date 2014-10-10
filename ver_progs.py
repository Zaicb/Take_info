# -*- coding: utf-8 -*-
#      _   _        __   __
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

n = 0
try:
    while 1:
        reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
        sub_key = _winreg.EnumKey(reg, n)
        #mess = '|| ' + sub_key + ' : '
        #sys.stdout.write(mess)
        sub_key = '\\'+sub_key
        path = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'+sub_key
        reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, path)

        k = 0

        d_name = 'err_a'
        d_ver = 'err_a'
        i_path = 'err_a'

        try:
            while 1: # DisplayName InstallLocation
                key = _winreg.EnumValue(reg, k)

                if key[0] == 'DisplayName':
                    d_name = key[1]
                if key[0] == 'DisplayVersion':
                    d_ver = key[1]
                if key[0] == 'InstallLocation':
                    i_path = key[1]

                k += 1

            print ''
        except:
            print ''
        if d_name != 'err_a':
            sys.stdout.write(d_name)
        if d_ver != 'err_a':
            sys.stdout.write(' Ver[ ')
            sys.stdout.write(d_ver)
            sys.stdout.write('] ')
        if i_path != 'err_a':
            sys.stdout.write(' PATH[ ')
            sys.stdout.write(i_path)
            sys.stdout.write('] ')
        n += 1
except:
    print '\n[= end of reg =]'

raw_input('\nEnter to end...')