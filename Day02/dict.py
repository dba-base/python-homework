__author__ = "xiaoyu hao"

info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}

print(info)
#查询
print(info['stu1101'])
print(info.get('stu1104'))   #如果没有就输出None

#判断key是否在字典中,如果在显示True，不在显示False
print('stu1105' in info)   #info.has_key('stu1105')  python 2.x

#修改
info['stu1101'] = '武藤兰'
print(info['stu1101'])

#插入数据
info['stu1104'] = 'teacher cang'
print(info)
#删除

del info['stu1101']
info.pop('stu1102')
print(info)

print(''.ljust(150,'-')) #输出150个 -

#多级字典嵌套及操作

av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
print(av_catalog["大陆"]["1024"])
#ouput['全部免费,真好,好人一生平安', '服务器在国外,慢,可以用爬虫爬下来']


#setdefault 如果存在键值，则不做任何动作，如果不存在插入
av_catalog.setdefault('大陆',{'www.123.com':[1,2,3]})
av_catalog.setdefault('乌克兰',{'www.123.com':[1,2,3]})
print(av_catalog)


#update操作

a = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}

b = {'stu1101': "aaa",
     1:2,
     3:4}

a.update(b)
print(a)   #输出{'stu1101': 'aaa', 'stu1102': 'LongZe Luola', 'stu1103': 'XiaoZe Maliya', 1: 2, 3: 4}
print(a.items())  # 转换成列表 ：
# dict_items([('stu1101', 'aaa'), ('stu1102', 'LongZe Luola'), ('stu1103', 'XiaoZe Maliya'), (1, 2), (3, 4)])

#初始化一个字典，并初始化值为‘test'
c = dict.fromkeys([1,2,3],'test')
print(c)

print(''.ljust(150,'-'))
#字典的循环
#建议用第一种方式，高效
for i in info:
    print(i,info[i])

print(''.ljust(150,'-'))

for k,v in info.items():  #会先把dict转成list,数据里大时莫用
    print(k,v)

#读取文件内容并转换成列表
with open('db/shopping_list', 'r', encoding='UTF-8') as f:
    result = dict(line.strip().split(':') for line in f if line)
for i in result:
    print(i, result[i])



