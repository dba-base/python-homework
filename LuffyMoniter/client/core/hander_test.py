# __author__ = "xiaoyu hao"
#
# monitored_services = {
#     'host': {'192.168.2.128':
#                  ['root', 'oracle', 22,
#                   {'services':
#                     {
#                         'LinuxCPU':     ['LinuxCpuPlugin', 30],
#                         'LinuxLoad':['LinuxLoadPlugin', 60],
#                         'LinuxMemory':['LinuxMemoryPlugin', 9],
#                         'LinuxNetwork':['LinuxNetworkPlugin', 6]
#                     }}
#                   ],
#             '192.168.2.129':
#                   ['root', 'oracle', 22,
#                    {'services':
#                     {'LinuxCPU':['LinuxCpuPlugin', 30],
#                      'LinuxLoad':['LinuxLoadPlugin', 60],
#                      'LinuxMemory':['LinuxMemoryPlugin', 9],
#                      'LinuxNetwork':['LinuxNetworkPlugin', 6]
#                     }}]
#             }
#
#         }
#
# for service_name,val in monitored_services['host'].items():
#     print('service Name:',service_name)
#     print('val:',val[0:3])
#     print('=======================================================')
#     for service_name,val_plugin in val[3]['services'].items():
#         print(service_name)
#         print(val_plugin)

li = ['/dev/mapper/VolGroup-lv_root   27G   25G  347M  99% /',
      'tmpfs                         431M   80K  431M   1% /dev/shm',
      '/dev/sda1                     485M   40M  421M   9% /boot']

<<<<<<< HEAD
{'ip': '192.168.2.128',
 '/': ['27G', '25G', '347M', '99%'],
 '/dev/shm': ['431M', '80K', '431M', '1%'],
 '/boot': ['485M', '40M', '421M', '9%'],
 'status': 0, 
 'time': '2018-07-04 16:22'}
=======
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
>>>>>>> d841c496728554b89a5f20e1073fbaf9b852716a
