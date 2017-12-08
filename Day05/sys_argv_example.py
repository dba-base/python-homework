__author__ = "xiaoyu hao"

import sys

'''
sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径，所以参数从1开始
'''
def readfile(filename):
    ''' Print a file to the standard output. '''
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)
    f.close()


# Script starts from here
if len(sys.argv) < 2:
    print(' NO action specified.')
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print(' version 1.2 ')
    elif option == 'help':
        print('''This program prints files to the standard output.
             Any number of files can be specified.
             Options include:
             --version : Prints the version number
             --help     : Display this help''')
    else:
        print('Unknow option.')
else:
    for filename in sys.argv[1:]:
        readfile(filename)