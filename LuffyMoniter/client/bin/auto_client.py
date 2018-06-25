__author__ = "xiaoyu hao"

import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.path.join(BASEDIR)
from core.scripts import client

if __name__ == '__main__':
    client()