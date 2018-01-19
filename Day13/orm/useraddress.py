__author__ = "xiaoyu hao"

#backref说明
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey,create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
import pymysql

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:root@localhost:3306/test1?charset=utf8")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    fullname = Column(String(32))
    password = Column(String(32))

    def __repr__(self):
        return "<User(name='%s',fullname='%s',password='%s')>" % (self.name,self.fullname,self.password)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True)
    email_address = Column(String(32),nullable=False)
    user_id = Column(Integer,ForeignKey('users.id'))

    user = relationship("User",backref="add")
    # backref 反向查询，如果不加 backref，backref跟一个字符串，被用来反向调用
    # 只能通过address表查询user表的内容，而user表不能查询address表的内容，
    # 所谓的User类中不用定义relationship就可以通过 add 调用

    def __repr__(self):
        return "<Address(id= '%d',email_address='%s')>" % (self.id,self.email_address)

#Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#插入数据
# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', password='foobar'),
#     User(name='mary', fullname='Mary Contrary', password='xxg527'),
#     User(name='fred', fullname='Fred Flinstone', password='blah')])

# a1 = Address(email_address='111@126.com',user_id=1)
# a2 = Address(email_address='112@126.com',user_id=2)
# a3 = Address(email_address='113@126.com',user_id=3)
# a4 = Address(email_address='114@126.com',user_id=2)
#
# session.add_all([a1,a2,a3,a4])

#查询

print("通过用户查地址：")
add_obj = session.query(Address).filter_by(user_id = 2).first()
print(add_obj.user)

print("通过地址查用户：")
user_obj = session.query(User).filter_by(id = 3).first()
print(user_obj.add)   # user_obj 调用的是backref中的字符串

session.commit()