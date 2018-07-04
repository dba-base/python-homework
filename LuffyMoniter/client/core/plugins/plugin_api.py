#_*_coding:utf-8_*_
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)
print(BASEDIR)

from core.plugins.Linux import sysinfo,cpu,memory,network,host_alive,load,filesystem
# from plugins.oracle import sysinfo,cpu_mac,cpu,memory,network,host_alive

def LinuxCpuPlugin(**kwargs):
    return cpu.monitor(**kwargs)

def host_alive_check(**kwargs):
    return host_alive.monitor(**kwargs)

def LinuxNetworkPlugin(**kwargs):
    return network.monitor(**kwargs)

def LinuxMemoryPlugin(**kwargs):
    return memory.monitor(**kwargs)

def LinuxLoadPlugin(**kwargs):
    return load.monitor(**kwargs)

def LinuxFilesystemPlugin(**kwargs):
    return filesystem.monitor(**kwargs)
