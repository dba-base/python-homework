参考博客
http://www.cnblogs.com/weiman3389/p/6044972.html
http://www.cnblogs.com/0zcl/p/6352278.html
http://www.cnblogs.com/wrlinux/p/7051170.html


create table users (
    id int(10),
    username char(20),
    passwoord char(20),
    real_name char(20)
)

create table host_info(
    id int(10),
    ip char(20),
    username char(20),
    password char(20),
    port int(10),
    server_type char(20)
)

insert into host_info values(1,'192.168.2.110','root','oracle',22,'test');
insert into host_info values(2,'192.168.2.110','root','oracle',22,'test');
insert into host_info values(3,'192.168.2.110','root','oracle',22,'test');
insert into host_info values(4,'192.168.2.110','root','oracle',22,'test');


insert into host_info values(5,'192.168.2.110','root','oracle',22,'test');
insert into host_info values(6,'192.168.2.110','root','oracle',22,'test');
insert into host_info values(7,'192.168.2.110','root','oracle',22,'test');
insert into host_info values(8,'192.168.2.110','root','oracle',22,'test');
