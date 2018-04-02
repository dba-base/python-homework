from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@localhost/testdb",
                       encoding='utf-8', echo=True)

Base = declarative_base()

#Customer表有2个字段都关联了Address表

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])

'''
类似如下sql
CREATE TABLE customer (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(32), 
	billing_address_id INTEGER, 
	shipping_address_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(billing_address_id) REFERENCES address (id), 
	FOREIGN KEY(shipping_address_id) REFERENCES address (id)
)
'''

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(32))
    city = Column(String(32))
    state = Column(String(32))

Base.metadata.create_all(engine) #创建表结构