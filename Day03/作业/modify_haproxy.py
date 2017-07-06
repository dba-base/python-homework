__author__ = "xiaoyu hao"

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




def add():
    pass


# def delete():
#     pass
#
# def update():
#     pass

