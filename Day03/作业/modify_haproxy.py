__author__ = "xiaoyu hao"

import os
import time


#查找函数
def search(address):
    flag = False
    serarch_list = []
    with open("haproxy","r") as f:
        for line in f:
            if line.strip() == 'backend %s' %(address):    #找到查询的行
                flag = True
                continue
            elif line.strip().startswith('backend'):       #如果遇到下一个以backend开头的，就把flag改成false，不再进行插入
                flag = False
            elif flag and line.strip().startswith('server'):
                serarch_list.append(line.strip())
        if len(serarch_list) == 0:
            print('未找到')
    return serarch_list

#取得backend,并存入列表中
#获取到以backend开头的行，并通过split函数把行转换成列表，把backend后面的值放入列表backend_list中
def get_backend():
    backend_list = []
    with open("haproxy","r") as f:
        for line in f:
            if line.strip().startswith("backend"):
                backend_list.append(line.strip().split()[1])
    return backend_list

''' 
输入：
arg = {
        'bakend': 'www.oldboy.org',
        'record':{
            'server': '100.1.7.9',
            'weight': 20,
            'maxconn': 30
            }
        }
'''

#生成record字典
def record_dict():
    record_dict = {}
    server = input("Server:")
    weight = input("weight:")
    maxconn = input("maxconn")

    record_dict["server"] = server
    record_dict["weight"] = weight
    record_dict["maxconn"] = maxconn

    return record_dict

#添加记录
'''
1. 把原来文件的内容都写入到新文件
2. 把要增加的内容再写入到文件最后
3. 重命名文件
'''
def add(bakend):
    #取得文件中所有backend值，并放入列表
    backend_list = get_backend()
    bakend_value = "backend %s" %bakend
    time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

    # 判断backend是否已经存在
    if bakend in backend_list:
        print("记录已存在！")
    else:
        record = record_dict()
        add_record = "server %s weight %s maxconn %s"\
                     % (record['server'], record["weight"], record["maxconn"])
        with open("haproxy","r") as read_f,\
             open("haproxy_new","w") as write_f:
            for line in read_f:
                write_f.write(line)
            write_f.write("\n"+bakend_value+"\n")
            temp = " "*8 + add_record +"\n"
            write_f.write(temp)
        #修改后让新的文件生效，旧文件下线
        os.rename("haproxy", "haproxy.bak%s" %time_str)
        os.rename("haproxy_new","haproxy")

#删除记录
'''
1.通过第一个查找函数，把要删除的记录放入到一个列表中
2.然后把不在这个列表中的内容在写入到新文件中
3.重命名文件
'''
def delete(backend):

    #取得文件中所有backend值，并放入列表
    backend_list = get_backend()
    record_li = search(backend)
    bakend_value = "backend %s" % backend
    record_li.insert(0,bakend_value)   # 把backend也加入到列表中
    print(record_li)

    time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

    # 判断backend是否已经存在
    if backend in backend_list:
        with open("haproxy", "r") as read_f, open("haproxy_new", "w") as write_f:
            for line in read_f:
                if line.strip() not in record_li:
                    write_f.write(line)

        os.rename("haproxy", "haproxy.bak%s" % time_str)
        os.rename("haproxy_new", "haproxy")

# def update():
#     pass


def main():
    msg = ''' 
    1. search
    2. add
    3. delete
    4. quit
    '''
    while True:
        print(msg)
        user_choice = input("Please input your choice: ")

        if user_choice == '1':
            backend = input("Please input backend(Example:www.oldboy.org): ")
            serarch_list = search(backend)
            for i in serarch_list:
                print(i)
        elif user_choice == "2":
            backend = input("Please input backend(Example:www.oldboy.org): ")
            #add_record = "server %s weight %s maxconn %s" % (record['server'], record["weight"], record["maxconn"])
            #print(add_record)
            add(backend)
        elif user_choice == "3":
            backend = input("Please input backend(Example:www.oldboy.org): ")
            delete(backend)
        elif user_choice in "4 q Q":
            exit()

        else:
            print("输入错误，请重新输入！")

if __name__ == '__main__':
    main()


