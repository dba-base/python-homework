__author__ = "xiaoyu hao"

import os,sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

print(BASEDIR)
from core import scripts

if __name__ == '__main__':
    scripts.command_handler(sys.argv)