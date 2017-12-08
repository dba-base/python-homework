
##############
#Oracle
##############

# 需要执行的sql语句字符串
DB_STATUA = '''select instance_name,status from gv$instance;'''

TABLESPACE_USED = '''
set line 150
set pages 999
Select a.Tablespace_Name,
       a.Total || 'M' Total_Space,
       (a.Total - b.Free) || 'M' Used_Space,
       To_Char((a.Total - b.Free) / a.Total * 100, '99.99') || '%' Pct_used
  From (Select Tablespace_Name, Sum(Bytes) / 1024 / 1024 Total
          From Dba_Data_Files
         Group By tablespace_Name) a,
       (Select Tablespace_Name, Sum(Bytes) / 1024 / 1024 Free
          From Dba_Free_Space
         Group By Tablespace_Name) b
where a.Tablespace_Name = b.Tablespace_Name;
'''


#key 界面显示，value 上面字符串名
DBMSG_DICT = {'DATABASE_STATUS':DB_STATUA,
              'TABLESPACE_USAGE':TABLESPACE_USED,
              '返回上一页':'1',
              '退出':'QUIT'
              }

########################################
#   OS 把需要执行的命令添加到下面的字典里
########################################

OSMSG_DICT = {'df':'df',
              'ifconfig':'ifconfig',
              'ls -l':'ls -l',
              '返回上一页':'1',
              '退出':'QUIT'
              }



# insert into host_info values(1,'192.168.2.110','root','oracl',22,'test');
# insert into host_info values(1,'192.168.3.110','root','oracl',22,'test');

#INSERT INTO host_info1 VALUES (1,'192.168.2.110','root', ENCODE('oracle', 'abcd'),22,'test');

#INSERT INTO host_info1 VALUES (2,'192.168.2.110','root', password('oracle'),22,'test');


'''
create table host_info2(id int(10),
ip char(20),
username char(20),
password blob,
port int(10),
server_type char(20)
);
INSERT INTO host_info2 VALUES (1,'192.168.2.110','root', ENCODE('oracle', 'abcd'),22,'test');
select id,ip,username,decode(password,'abcd'),port,server_type from host_info2;
'''
