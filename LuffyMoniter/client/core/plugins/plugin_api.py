#_*_coding:utf-8_*_
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)
print(BASEDIR)

from core.plugins.Linux import sysinfo,cpu,memory,network,host_alive,load
# from plugins.oracle import sysinfo,cpu_mac,cpu,memory,network,host_alive

def LinuxCpuPlugin():
    return cpu.monitor()

def host_alive_check():
    return host_alive.monitor()

def LinuxNetworkPlugin():
    return network.monitor()

def LinuxMemoryPlugin():
    return memory.monitor()

def LinuxLoadPlugin():
    return load.monitor()
