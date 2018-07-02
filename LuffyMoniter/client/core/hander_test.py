__author__ = "xiaoyu hao"


monitored_services = {'services':
                                       {'LinuxCPU':
                                            ['LinuxCpuPlugin',60],
                                        'LinuxLoad':
                                            ['LinuxLoadPlugin',30],
                                        'LinuxMemory':
                                            ['LinuxMemoryPlugin',90],
                                        'LinuxNetwork':
                                            ['LinuxNetworkPlugin',60]
                                        },
                                   'host':{'192.168.2.128':['root','oracle'],'192.168.233.128':['root','oracle']}
                                   }




for ip_key,val in monitored_services['host'].items():
    host = {ip_key:val}
    print(host)
