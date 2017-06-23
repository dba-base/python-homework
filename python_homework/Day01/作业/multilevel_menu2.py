#Author: xiaoyu hao

'''
实现功能
1.三级菜单
2.可依次选择进入各子菜单，并打印对应内容

知识体现：
字典的循环遍历
'''

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

#如果退出，设置exit_flag 为 True，即退出整个循环
exit_flag = False
while not exit_flag:
    select_msg = '''
        --------------------------------------------------------------
                        中国七大地理地区分布查询系统
        1. 显示中国地理分布
        4. 退出（q/Q）
        --------------------------------------------------------------
    '''
    print(select_msg)
    userinput = input("请输入选项：")
    if userinput == "1":
        #第一层菜单
        for i in map_dict:
            print(i)
        choise1 = input("选择要打印的区域：")
        #第二层菜单
        if choise1 in map_dict:
            while not exit_flag:
                for i in map_dict[choise1]:
                    print(i)
                choise2 = input("选择要打印的省份：")
                #第三层菜单
                if choise2 in map_dict[choise1]:
                    while not exit_flag:
                        for i in map_dict[choise1][choise2]:
                            print(i)
                        #退出校验
                        choise3 = input("最后一层，输入b上一层，q退出：")
                        if choise3 == "b":
                            break
                        elif choise3 == "q":
                            exit_flag = True
                        else:
                            print("输入错误，请重新输入！")
                elif choise2 == "b":  #返回上级菜单
                    break
                elif choise2 == "q":  #退出程序
                    exit_flag = True
                else:
                    print("%s 不存在或者输入错误！" % choise2)
        elif choise1 == "b" or choise1 == "q":
            print("系统退出！")
            break
        else:
            print("%s 不存在或者输入错误！" % choise1)
    elif userinput in ["4","q","Q"]:
        print("退出系统")
        exit()

