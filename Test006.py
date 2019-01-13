import ctypes

calc = ("c:\windows\system32\\calc.exe")
notepad = ("c:\windows\system32\\notepad.exe")
paint = ("c:\windows\system32\\mspaint.exe")

#ctypes.windll.shell32.ShellExecuteEx(0, 'open', calc, None, None, 1)
ctypes.windll.shell32.ShellExecuteA(0, 'open', calc, None, None, 1)