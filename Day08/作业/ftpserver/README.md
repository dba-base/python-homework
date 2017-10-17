 ### 功能实现
    作业：开发一个支持多用户在线的FTP程序
    要求：
        1.用户加密认证
        2.允许同时多用户登录
        3.每个用户有自己的家目录 ，且只能访问自己的家目录
        4.对用户进行磁盘配额，每个用户的可用空间不同
        5.允许用户在ftp server上随意切换目录
        6.允许用户查看当前目录下文件
        7.允许上传和下载文件，保证文件一致性
        8.文件传输过程中显示进度条
        9.附加功能：支持文件的断点续传

 ### 目录结构
 FTP
    │
    ├── ftpclient #客户端程序
    │      ├── __init__.py
    │      └── ftpclient.py  #客户端主程序
    └── ftpserver #服务端程序
            ├── README.txt
            ├── bin
			│   ├── __init__.py
			│   └── ftpserver.py #服务端入口程序
            ├── conf #配置文件目录
            │   ├── __init__.py
            │   └── setting.py
            ├── src  #程序核心目录
            │   ├── __init__.py
            │   ├── auth_user.py  #用户认证模块
            │   └── sokect_server.py  #sokectserver模块
            ├── data #用户数据库
            │   ├── alex.db
            │   ├── lzl.db
            │   └── eric.db
            ├── home #用户宿主目录
            │   ├── alex
            │   ├── lzl
            │   └── eric
            └── log
                ├── __init__.py
                └── log  #待扩展....