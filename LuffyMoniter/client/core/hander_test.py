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
                                   'host':{'192.168.2.128':['root','oracle']}
                                   }

for service_name,val in monitored_services['services'].items():
    print('service Name:',service_name)
    print('val:',val)

for ip,img in monitored_services['host'].items():
    print('ip:',ip)
    print('img:',img)