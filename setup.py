import sys
import os
import shutil
import getpass
import subprocess

def check_for_crontab():
    # '-l', '>', '$PWD/tmp_crontab'
    crontab_list = ['crontab', '-l']
    pipe = subprocess.run(crontab_list, stdout=subprocess.PIPE)    
    # print(pipe.stdout, len(pipe.stdout))
    # If the length of the crontab pipe is larger than 0, it has content.     
    if len(pipe.stdout) > 0:
        # Write pipe to a local file as binary 
        with open('tmp_crontab', 'a+b') as crontab:
            # lines = crontab.readlines()
            crontab.write(pipe.stdout)
        # os.remove('tmp_crontab')

        return True

    return False

def main():

    # Maybe no Run two times?
    print('Would you like to enable the script to check for updates at startup?')
    auto_update_checker = input('Would you like to enable this ? (Y/N) > ')
    
    if sys.platform == 'linux' or sys.platform == 'linux2':
        # linux
        print('It seems like you are on a linux dist')
        os.system(f'bash {os.getcwd()}/setup-linux.sh')
        if auto_update_checker == "Y":
            if check_for_crontab():
                # TODO: Fix so it appends to crontab but if it already has this content of 'updater' it wont update it
                print("Crontab already exists, saved content to 'tmp_crontab'")
                # with open('tmp_crontab', 'a+b'):
            else:
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
