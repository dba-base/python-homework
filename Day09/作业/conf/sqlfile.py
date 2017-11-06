
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


DBMSG_DICT = {'DATABASE_STATUS':DB_STATUA,
              'TABLESPACE_USAGE':TABLESPACE_USED}

# for i in DBMSG_DICT:
#     print(i)
#     print(DBMSG_DICT.get(i))




