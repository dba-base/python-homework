class Role(object):

    nationality = "JP"  #类的公有属性

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.__heart = "Normal"  #私有属性,只能在类的内部调用

    def shot(self):   #公有方法
        print("shooting..." %self.name)

    def got_shot(self):
        print("ah...,I got shot...")
        self.__heart = 'Die'
        print(self.__heart)

    def get_heart(self):    #提供访问私有属性接口
        return self.__heart

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)

    def __del__(self):
        print("del ... run ....")


r1 = Role('Alex', 'police', 'AK47') #生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色

print(r1.name)
print(r1.got_shot())


r = r1.get_heart()  #访问私有属性
print(r)

r1._Role__heart   #强制访问私有属性

#访问公有属性
Role.nationality = "US"  #修改类的公有属性
r2.nationality = "Thailand"  #重载公有属性
print(r1.nationality)
print(r2.nationality)


def shot2(self):   #私有方法
    print("use my own method",self.name)

r1.shot = shot2

r1.shot(r1)   #需要手动传入r1实例
