#Author: xiaoyu hao

'''
实现功能
1.三级菜单
2.可依次选择进入各子菜单，并打印对应内容

知识体现：
字典和列表的转换
'''

'''代码很low，实现了基本功能，还需改进'''

map_dict = \
    {'华东':
         {'上海市':['上海','浦东'],
          '江苏省':['南京'],
          '浙江省':['杭州'],
          '安徽省':['合肥'],
          '福建省':['福州'],
          '江西省':['南昌'],
          '山东省':['济南'],
          '台湾省':['台北']
          },
     '华北':
         {'北京市':['北京'],
          '天津市':['天津'],
          '山西省':['太原','忻州','大同','朔州'],
          '河北省':['石家庄'],
          '内蒙古自治区中部':['呼和浩特']},
     '华中':
         {'河南省':['郑州'],
          '湖北省':['武汉'],
          '湖南省':['长沙']},
     '华南':
         {'广东省':['广州'],
          '广西壮族自治区':['桂林'],
          '海南省':['海口'],
          '香港特别行政区':['香港'],
          '澳门特别行政区':['澳门']},
     '西南':
         {'四川省':['成都'],
          '贵州省':['贵阳'],
          '云南省':['昆明'],
          '重庆市':['重庆'],
          '西藏自治区':['拉萨']},
     '西北':
         {'陕西省':['西安'],
          '甘肃省':['兰州'],
          '青海省':['西宁'],
          '宁夏回族自治区':['银川'],
          '新疆维吾尔自治区':['乌鲁木齐'],
          '内蒙古自治区西部':[]},
     '东北':
         {'黑龙江省':['哈尔滨'],
          '吉林省':['长春'],
          '辽宁省':['沈阳'],
          '内蒙古自治区东部':[]}
    }

num = 1
exit_flag = False

def display():
    select_msg = '''
        --------------------------------------------------------------
                        中国七大地理地区分布查询系统
        1. 显示中国地理分布
        4. 退出（q/Q）
        --------------------------------------------------------------
    '''
    return select_msg

#字典转换列表,输出 [(0, '华东'), (1, '华北'), (2, '华中'), (3, '华南'), (4, '西南'), (5, '西北'), (6, '东北')]
ch_district = [(index, key) for index, key in enumerate(map_dict)]

while not exit_flag:
    dis=display()
    print(dis)
    userinput = input("请输入要查询的编号：")
    while not exit_flag:
        if userinput == "1":
            #从字典map_dict中，打印key，即地区
            for dist in map_dict.keys():
                print("%s. %s" %(num,dist))
                num+=1
            distnum = input("请输入地区前面得数字进行检索(输入%s返回上一层),输入0退出系统："%num)
            #第一层
            if not distnum.isdigit():
                print("输入错误，请输入数字。。。")
                num = 1
                continue
            elif int(distnum) > len(map_dict)+1:
                print("编号越界@@@@")
                num = 1
                continue
            elif int(distnum) == len(map_dict)+1:
                num = 1
                break
            elif distnum == '0':
                exit_flag = True
            else:
                num = 1
                while not exit_flag:
                    #列表中显示选中的地区名
                    choose_dict = ch_district[int(distnum)-1][1]
                    # 创建省会城市列表
                    city_li = [(index,key) for index,key in enumerate(map_dict[choose_dict])]
                    #取出的字典赋值给province_map
                    province_map = map_dict[choose_dict]
                    province_num = 1
                    print("%s地区 包含以下省："%choose_dict)
                    #对应地区显示包含的所有省
                    for province in province_map.keys():
                        print("%s. %s" % (province_num, province))
                        province_num+=1
                    citynum = input("请输入相应的数字进行检索，输入%s返回上一层。输入0退出系统："%province_num)
                    #第二层
                    if not citynum.isdigit():
                        print("输入错误，请输入数字。。。")
                        citynum = 1
                        continue
                    elif int(citynum) > len(province_map)+1:
                        print("编号越界@@@@")
                        citynum = 1
                        continue
                    elif int(citynum) == len(province_map)+1:
                        citynum = 1
                        break
                    elif citynum == '0':
                        exit_flag = True
                    else:
                        citynum = 1
                        while not exit_flag:
                            #选择的省
                            choose_province = city_li[int(citynum)-1][1]
                            city_num = 1
                            #显示对应省包含的城市
                            for city in province_map[choose_province]:
                                print("%s. %s" % (city_num, city))
                                city_num += 1
                            chose_end = input("返回上一层：（b/B）,(q)退出")
                            if chose_end == "b":
                                break
                            elif chose_end == "q":
                                exit_flag = True
        elif userinput == "4":
            exit()
        else:
            print("输入错误！请重新输入！")
            break