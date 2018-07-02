#_*_coding:utf-8_*_
import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASEDIR)
print(BASEDIR)

from core.plugins.Linux import sysinfo,cpu,memory,network,host_alive,load
# from plugins.oracle import sysinfo,cpu_mac,cpu,memory,network,host_alive

<<<<<<< HEAD
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


# if __name__ == '__main__':
#     # if __name__ == '__main__':
#     host_message = {'192.168.231.110': ['root', 'oracle', 22]}
#     a=LinuxCpuPlugin(**host_message)
#     print(a)
#     b=host_alive_check(**host_message)
#     print(b)
=======
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
>>>>>>> 6ecfbf47f8803bc2f0083c090b9bb3c2d7d16b96
