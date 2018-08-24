__author__ = "xiaoyu hao"

#导入SQLite驱动
import sqlite3
#连接到SQlite数据库
#数据库文件是test.db，不存在，则自动创建
sql1='CREATE TABLE "test1" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "hostname" varchar(64) NOT NULL, "instance_name" varchar(64) NOT NULL, "ip_addr" char(39) NOT NULL UNIQUE, "port" smallint unsigned NOT NULL, "db_port" smallint unsigned NULL, "username" varchar(64) NOT NULL, "db_username" varchar(64) NOT NULL, "password" varchar(128) NULL, "db_password" varchar(128) NULL, "database_type" smallint NOT NULL, "os_type" smallint NOT NULL, "enabled" bool NOT NULL, "is_database" bool NOT NULL, "appcompany_id" integer NOT NULL REFERENCES "web_appcompany" ("id") DEFERRABLE INITIALLY DEFERRED, "business_id" integer NOT NULL REFERENCES "web_business" ("id") DEFERRABLE INITIALLY DEFERRED, "idc_id" integer NOT NULL REFERENCES "web_idc" ("id") DEFERRABLE INITIALLY DEFERRED, "comment" varchar(128) NULL)'
conn = sqlite3.connect('../db.sqlite3')
#创建一个cursor：
cursor = conn.cursor()
#执行一条SQL语句：创建user表
cursor.execute(sql1)
#插入一条记录：
cursor.execute('insert into test1 (id, name) values (\'1\', \'Michael\')')
#通过rowcount获得插入的行数：
print(cursor.rowcount) #reusult 1
#关闭Cursor:
cursor.close()
#提交事务：
conn.commit()
#关闭connection：
conn.close()
