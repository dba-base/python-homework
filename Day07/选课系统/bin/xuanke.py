__author__ = "xiaoyu hao"

'''

'''
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)

from conf import settings
from core import main

if __name__ == '__main__':
    sch_obj = main.Center()
    sch_obj.run()