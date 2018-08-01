#_*_coding:utf-8_*_
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)
print(BASEDIR)

from core.plugins.oracle import db
# from plugins.oracle import sysinfo,cpu_mac,cpu,memory,network,host_alive

def OraclePlugin(**host_message):
    return db.monitor(**host_message)

