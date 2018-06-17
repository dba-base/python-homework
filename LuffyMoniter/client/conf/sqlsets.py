__author__ = "xiaoyu hao"

SQLSTATUS='select * from dual'
TABLESPACE_SQL='''
Select a.Tablespace_Name, Total, Free, Total - Free Used
  from ( Select Tablespace_Name, Sum (Bytes) / 1024 / 1024 Total
          From Dba_Data_Files
         group By Tablespace_Name) a,
       ( Select Tablespace_Name, Sum (Bytes) / 1024 / 1024 Free
          From Dba_Free_Space
         group By Tablespace_Name) b
 where a.Tablespace_Name = b.Tablespace_Name
'''
