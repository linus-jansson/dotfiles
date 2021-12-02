import sys
import os
import shutil
import getpass
import traceback
import types


# https://stackoverflow.com/questions/19672352/how-to-run-script-with-elevated-privilege-on-windows
# https://stackoverflow.com/questions/4553129/when-to-use-os-name-sys-platform-or-platform-system
def isUserAdmin():
    if os.name == "nt":
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError("Unsupported operating system for this module: %s" % (os.name,))

def runAsAdmin(cmdLine=None, wait=True):
    python_exe = sys.executable

    if os.name == 'possix':
        os.system(f"sudo {sys.executable} setup.py")
        # raise RuntimeError("This function is only implemented on Windows.")

    elif os.name == "nt":

        import win32api, win32con, win32event, win32process
        from win32com.shell.shell import ShellExecuteEx
        from win32com.shell import shellcon

        if cmdLine is None:
            cmdLine = [python_exe] + sys.argv
        elif type(cmdLine) not in (types.TupleType,types.ListType):
            raise ValueError("cmdLine is not a sequence.")
        cmd = '"%s"' % (cmdLine[0],)
        # XXX TODO: isn't there a function or something we can call to massage command line params?
        params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
        cmdDir = ''
        showCmd = win32con.SW_SHOWNORMAL
        #showCmd = win32con.SW_HIDE
        lpVerb = 'runas'  # causes UAC elevation prompt.

        # print "Running", cmd, params

        # ShellExecute() doesn't seem to allow us to fetch the PID or handle
        # of the process, so we can't get anything useful from it. Therefore
        # the more complex ShellExecuteEx() must be used.

        # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

        procInfo = ShellExecuteEx(nShow=showCmd,
                                fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                                lpVerb=lpVerb,
                                lpFile=cmd,
                                lpParameters=params)

        if wait:
            procHandle = procInfo['hProcess']    
            obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
            rc = win32process.GetExitCodeProcess(procHandle)
            #print "Process handle %s returned code %s" % (procHandle, rc)
        else:
            rc = None

        return rc
    else:
        raise RuntimeError("Unsupported operating system for this module: %s" % (os.name,))


def generate_git_checker():
    # Cool :D
    with open("git-pull-on-boot.py", "w+") as script:
        cmds = ["import os, sys", f"os.system(f'cd {os.getcwd()} && {sys.executable} update.py')"]
        for i in cmds:
            script.write(i + '\n')

def main():
    
    if not isUserAdmin():
        rc = runAsAdmin()

    # Maybe no Run two times?
    print('Would you like to enable the script to check for updates at startup?')
    auto_update_checker = input('Would you like to enable this ? (Y/N) > ')
    
    if auto_update_checker == "Y":
        generate_git_checker()

    if sys.platform == 'linux' or sys.platform == 'linux2':
        # linux
        print('linux')
        os.system(f'bash {os.getcwd()}/setup-linux.sh')
        if isUserAdmin() and auto_update_checker == 'Y':
            print('We are admin')
    elif sys.platform == 'win32':
        # Windows...
        os.system(f'{os.getcwd()}\setup-windows.bat')
        # checkForAdmin() and 
        if isUserAdmin() and auto_update_checker == 'Y':
            print('We are admin')
            print('Placing config updater in shell:autostart')
            user = getpass.getuser()
            path = r'C:\Users\\' + user + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
            shutil.copy('setup-windows.bat', path)
    else:
        print('No valid system found')

    input('Press any key to continue...')

if __name__ == '__main__':
    main()