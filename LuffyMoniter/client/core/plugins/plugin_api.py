#_*_coding:utf-8_*_
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)
print(BASEDIR)

from core.plugins.Linux import sysinfo,cpu,memory,network,host_alive,load,filesystem
from core.plugins.oracle import OraTBS


def LinuxCpuPlugin(**host_message):
    return cpu.monitor(**host_message)

def host_alive_check(**host_message):
    return host_alive.monitor(**host_message)

def LinuxNetworkPlugin(**host_message):
    return network.monitor(**host_message)

def LinuxMemoryPlugin(**host_message):
    return memory.monitor(**host_message)

def LinuxLoadPlugin(**host_message):
    return load.monitor(**host_message)

def LinuxFilesystemPlugin(**host_message):
    return filesystem.monitor(**host_message)

def OraTBSPlugin(**host_message):
    return OraTBS.monitor(**host_message)

