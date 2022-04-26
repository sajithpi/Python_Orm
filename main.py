from requests import Session
from sqlalchemy import Column, ForeignKey,String,Integer,DateTime,create_engine,exc,desc
# from sqlalchemy.ext.declarative import declarative_base       
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from datetime import datetime


Base = declarative_base()

# Specifying database connection url
engine = create_engine("mysql://root:password@localhost/orm_join",echo=True)

Session = sessionmaker()

# Table creation
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),primary_key=True)
    username = Column(String(25),nullable=False,unique=True)
    email = Column(String(75),unique=True,nullable=False)
    date_created = Column(DateTime(),default=datetime.utcnow)
    # child = relationship('profile','amount',backref='users',uselist=False)

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer(),primary_key=True)
    user_id = Column(Integer(),ForeignKey('users.id'))
    sponser_id=Column(Integer(),nullable=False)
    address = Column(String(25),nullable=False)
 

class Account(Base):
    __tablename__='account'
    id = Column(Integer(),primary_key=True)
    user_id = Column(Integer(),ForeignKey('users.id'))
    balance = Column(Integer())
           
                                                                                                                                              