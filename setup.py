import sys
import os
import shutil
import getpass


def main():

    # Maybe no Run two times?
    print('Would you like to enable the script to check for updates at startup?')
    auto_update_checker = input('Would you like to enable this ? (Y/N) > ')
    
    if sys.platform == 'linux' or sys.platform == 'linux2':
        # linux
        print('It seems like you are on a linux dist')
        os.system(f'bash {os.getcwd()}/setup-linux.sh')
        if auto_update_checker == "Y":
           os.system('crontab updater')

    # WIP
    elif sys.platform == 'win32':
        # Windows...
        os.system(f'{os.getcwd()}\setup-windows.bat')
        if auto_update_checker == 'Y':
            print('We are admin')
            print('Placing config updater in shell:autostart')
            user = getpass.getuser()
            path = r'C:\Users\\' + user + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
            shutil.copy('setup-windows.bat', path)
    else:
        print('No valid system found')

    input('\nPress any key to continue...\n')

if __name__ == '__main__':
    main()
