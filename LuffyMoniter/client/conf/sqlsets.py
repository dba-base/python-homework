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

PATCH_SQL = '''
select * from dba_registry_history
'''

DB_TIME = '''
SELECT * FROM
(
SELECT
  A.INSTANCE_NUMBER,
  LAG(A.SNAP_ID) OVER (ORDER BY A.SNAP_ID) BEGIN_SNAP_ID,
  A.SNAP_ID END_SNAP_ID,
  TO_CHAR(B.BEGIN_INTERVAL_TIME,'DD-MON-YY HH24:MI') SNAP_BEGIN_TIME,
  TO_CHAR(B.END_INTERVAL_TIME ,'DD-MON-YY HH24:MI') SNAP_END_TIME,
  ROUND((A.VALUE-LAG(A.VALUE) OVER (ORDER BY A.SNAP_ID ))/1000000/60,2) DB_TIME_MIN
FROM
DBA_HIST_SYS_TIME_MODEL A, DBA_HIST_SNAPSHOT B
WHERE
A.SNAP_ID = B.SNAP_ID AND
A.INSTANCE_NUMBER = B.INSTANCE_NUMBER AND
A.STAT_NAME = 'DB time'
)
WHERE DB_TIME_MIN IS NOT NULL AND DB_TIME_MIN > 0
ORDER BY 2 DESC
'''

TOP10EVENT='''
SELECT * FROM (
SELECT EVENT,TOTAL_WAITS,AVERAGE_WAIT,TIME_WAITED 
FROM v$system_event WHERE wait_class<>'Idle' 
ORDER BY time_waited desc)  WHERE rownum<=10
'''

