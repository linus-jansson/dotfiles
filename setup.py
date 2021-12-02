import sys
import os
import ctypes

# Check for git changes on system boot

def checkForAdmin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if sys.platform == "linux" or sys.platform == "linux2":
    # linux
    print("linux")
    os.system('chmod +x setup-linux.sh && setup-linux.sh')
    if checkForAdmin():
        print("We are admin")

elif sys.platform == "darwin":
    # OS X (NOT USING MAC lel)
    pass
elif sys.platform == "win32":
    # Windows...
    os.system('setup-windows.bat')
    if checkForAdmin():
        print("We are admin")
else:
    print("No valid system found")
