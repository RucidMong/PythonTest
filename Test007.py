import os
import subprocess
import _thread

calc = ("c:\windows\system32\\calc.exe")
notepad = ("c:\windows\system32\\notepad.exe")
paint = ("c:\windows\system32\\mspaint.exe")

def os_system(path):
    os.system(path)

def os_popen(path):
    os.popen(path)

_thread.start_new_thread(os_system, (calc,))sB
_thread.start_new_thread(os_popen, (notepad,))

subprocess.call(paint)