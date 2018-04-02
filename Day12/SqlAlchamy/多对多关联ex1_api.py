
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,query
from Day12.SqlAlchamy import 多对多关联ex1 as m2m

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:root@localhost/testdb?charset=utf8",
                       echo=True)

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
s = Session_class()  # 生成session实例

'''
#insert data
b1 = m2m.Book(name="Python",pub_date="2017-12-12")
b2 = m2m.Book(name="mysql",pub_date="2017-12-12")
b3 = m2m.Book(name="oracle",pub_date="2017-12-12")
b4 = m2m.Book(name="docker",pub_date="2017-12-12")

a1 = m2m.Author(name="Alex")
a2 = m2m.Author(name="Jack")
a3 = m2m.Author(name="Rain")

b1.authors = [a1, a2]
b2.authors = [a1, a2, a3]

s.add_all([b1, b2, b3, b4, a1, a2, a3])
'''

#查询作者出版的所有书籍
print('--------通过作者表查关联的书---------')
author_obj = s.query(m2m.Author).filter_by(name="Alex").first()
print("author_obj的值：",author_obj)
print(author_obj.name,author_obj.books)

print('--------通过书表查关联的作者---------')
book_obj = s.query(m2m.Book).filter_by(name="Python").first()
print(book_obj.name, book_obj.authors)
s.commit()