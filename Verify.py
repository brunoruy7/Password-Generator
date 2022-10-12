# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:08:12 2022

@author: BRUNO
"""

from tkinter import *


def verificaAdmin():
    import os
    import sys, ctypes
    import win32com.shell.shell as shell
    ASADMIN = 'asadmin'
    # print(sys.executable)
    # teste = "D:\Pastas\Projects\RandomPasswordGenerator\verify.exe"
    # if sys.argv[-1] != ASADMIN:
    #     script = os.path.abspath(sys.argv[0])
    #     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    #     shell.ShellExecuteEx(lpVerb='runas', lpFile=teste, lpParameters=params)
    try:
        if ctypes.windll.shell32.isUserAdmin():
            ret = 50
    except:
        print('foi')
        ret = ctypes.windll.shell32.ShellExecuteW(None, "runas",
                                                  sys.executable,
                                                  " ".join(sys.argv), None, 0)
        print(ret)
    for widget in sys.executable.winfo_children():
        widget.destroy()


if __name__ == '__main__':
    verificaAdmin()
