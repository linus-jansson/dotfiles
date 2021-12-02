import os, sys
def main():
    if sys.platform == 'linux' or sys.platform == 'linux2':
        os.system(f'bash {os.getcwd()}/setup-linux.sh')
    elif sys.platform == 'win32':
        os.system(f'{os.getcwd()}\setup-windows.bat')
    else:
        print('No valid system found')

if __name__ == '__main__':
    main()