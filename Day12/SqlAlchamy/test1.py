import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:root@localhost/testdb",
                       encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    # 格式化输出
    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (
            self.name, self.password)

#1. 创建表
Base.metadata.create_all(engine)  # 创建表结构


#2. 插入数据
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
print(user_obj.name, user_obj.id)  # 此时也依然还没创建

Session.commit()  # 现此才统一提交，创建数据


#3. 查询

my_user = Session.query(User).filter_by(name="alex").first()
print(my_user)


#4. 修改

my_user = Session.query(User).filter_by(name="alex").first()

my_user.name = "Alex Li"

Session.commit()

#5. 查询所有数据
print(Session.query(User.name,User.id).all() )


#6. 外建关联

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", backref="addresses")  # 这个nb，允许你在user表里通过backref字段反向查出所有它在addresses表里的关联项

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

Base.metadata.create_all(engine)

obj = Session.query(User).first()
for i in obj.addresses:  # 通过user对象反查关联的addresses记录
    print(i)

addr_obj = Session.query(Address).first()
print(addr_obj.user.name)  # 在addr_obj里直接查关联的user表