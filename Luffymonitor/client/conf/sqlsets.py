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
select * from dba_registry_history order by  action_time desc
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

DBSIZE='''
select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') ,a.Total_size,b.segment_size,c.instance_name,free.poo Free from 
(select sum(bytes/1024/1024/1024) Total_size from (select bytes from v$datafile
union all
select bytes from  v$tempfile
union  all
select  bytes from  v$log)) a,
(select sum(bytes/1024/1024/1024) segment_size from dba_segments) b,
(select instance_name,VERSION,ARCHIVER,STARTUP_TIME from v$instance) c,
(select sum(bytes/1024/1024/1024) as poo from dba_free_space) free
'''

DBWAIT_EVENT='''
select t2.event,
       round(100 * t2.time_waited / (t1.w1 + t3.cpu), 2) event_wait_percent
  from (SELECT SUM(time_waited) w1
          FROM v$system_event
         WHERE event NOT IN
               ('smon timer',
                'pmon timer',
                'rdbms ipc message',
                'Null event',
                'parallel query dequeue',
                'pipe get',
                'client message',
                'SQL*Net message to client',
                'SQL*Net message from client',
                'SQL*Net more data from client',
                'dispatcher timer',
                'virtual circuit status',
                'lock manager wait for remote message',
                'PX Idle Wait',
                'PX Deq: Execution Msg',
                'PX Deq: Table Q Normal',
                'wakeup time manager',
                'slave wait',
                'i/o slave wait',
                'jobq slave wait',
                'null event',
                'gcs remote message',
                'gcs for action',
                'ges remote message',
                'queue messages',
                'wait for unread message on broadcast channel',
                'PX Deq Credit: send blkd',
                'PX Deq: Execute Reply',
                'PX Deq: Signal ACK',
                'PX Deque wait',
                'PX Deq Credit: need buffer',
                'STREAMS apply coord waiting for slave message',
                'STREAMS apply slave waiting for coord message',
                'Queue Monitor Wait',
                'Queue Monitor Slave Wait',
                'wakeup event for builder',
                'wakeup event for preparer',
                'wakeup event for reader',
                'wait for activate message',
                'PX Deq: Par Recov Execute',
                'PX Deq: Table Q Sample',
                'STREAMS apply slave idle wait',
                'STREAcapture process filter callback wait for ruleset',
                'STREAMS fetch slave waiting for txns',
                'STREAMS waiting for subscribers to catch up',
                'Queue Monitor Shutdown Wait',
                'AQ Proxy Cleanup Wait',
                'knlqdeq',
                'class slave wait',
                'master wait',
                'DIAG idle wait',
                'ASM background timer',
                'KSV master wait',
                'EMON idle wait',
                'Streams AQ:RACqmn coordinator idle wait',
                'Streams AQ: qmn coordinator idle wait',
                'Streams AQ: qmn slave idle wait',
                'Streams AQ: waiting for time management or cleanup tasks',
                'Streams AQ: waiting for messages in the queue',
                'Streams fetch slave: waiting for txns',
                'Streams AQ:deallocate messages from Streams Pool',
                'Streams AQ: delete acknowledged messages',
                'LNS ASYNC archive log',
                'LNS ASYNC dest activation',
                'LNS ASYNC end of log',
                'LogMiner: client waiting for transaction',
                'LogMiner: slave waiting for activate message',
                'LogMiner: wakeup event for builder',
                'LogMiner: wakeup event for preparer',
                'LogMiner: wakeup event for reader')) t1,
       (select *
          from (select t.event,
                       t.total_waits,
                       t.total_timeouts,
                       t.time_waited,
                       t.average_wait,
                       rownum num
                  from (select event,
                               total_waits,
                               total_timeouts,
                               time_waited,
                               average_wait
                          from v$system_event
                         where event not in
                               ('smon timer',
                                'pmon timer',
                                'rdbms ipc message',
                                'Null event',
                                'parallel query dequeue',
                                'pipe get',
                                'client message',
                                'SQL*Net message to client',
                                'SQL*Net message from client',
                                'SQL*Net more data from client',
                                'dispatcher timer',
                                'virtual circuit status',
                                'lock manager wait for remote message',
                                'PX Idle Wait',
                                'PX Deq: Execution Msg',
                                'PX Deq: Table Q Normal',
                                'wakeup time manager',
                                'slave wait',
                                'i/o slave wait',
                                'jobq slave wait',
                                'null event',
                                'gcs remote message',
                                'gcs for action',
                                'ges remote message',
                                'queue messages',
                                'wait for unread message on broadcast channel',
                                'PX Deq Credit: send blkd',
                                'PX Deq: Execute Reply',
                                'PX Deq: Signal ACK',
                                'PX Deque wait',
                                'PX Deq Credit: need buffer',
                                'STREAMS apply coord waiting for slave message',
                                'STREAMS apply slave waiting for coord message',
                                'Queue Monitor Wait',
                                'Queue Monitor Slave Wait',
                                'wakeup event for builder',
                                'wakeup event for preparer',
                                'wakeup event for reader',
                                'wait for activate message',
                                'PX Deq: Par Recov Execute',
                                'PX Deq: Table Q Sample',
                                'STREAMS apply slave idle wait',
                                'STREAcapture process filter callback wait for ruleset',
                                'STREAMS fetch slave waiting for txns',
                                'STREAMS waiting for subscribers to catch up',
                                'Queue Monitor Shutdown Wait',
                                'AQ Proxy Cleanup Wait',
                                'knlqdeq',
                                'class slave wait',
                                'master wait',
                                'DIAG idle wait',
                                'ASM background timer',
                                'KSV master wait',
                                'EMON idle wait',
                                'Streams AQ: RAC qmn coordinator idle wait',
                                'Streams AQ: qmn coordinator idle wait',
                                'Streams AQ: qmn slave idle wait',
                                'Streams AQ: waiting for time management or cleanup tasks',
                                'Streams AQ: waiting for messages in the queue',
                                'Streams fetch slave: waiting for txns',
                                'Streams AQ:deallocate messages from Streams Pool',
                                'Streams AQ: delete acknowledged messages',
                                'LNS ASYNC archive log',
                                'LNS ASYNC dest activation',
                                'LNS ASYNC end of log',
                                'LogMiner: client waiting for transaction',
                                'LogMiner: slave waiting for activate message',
                                'LogMiner: wakeup event for builder',
                                'LogMiner: wakeup event for preparer',
                                'LogMiner: wakeup event for reader')
                         order by time_waited desc) t)
         where num < 11) t2,
       (SELECT VALUE CPU
          FROM v$sysstat
         WHERE NAME LIKE 'CPU used by this session') t3
'''


