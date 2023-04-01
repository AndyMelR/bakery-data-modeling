import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(300), nullable=False)
    password = Column (String(9), nullable=False)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
   


class Photo(Base):
    __tablename__ = 'photo'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    PhotoLocation = Column(String(300))
    CreationDate = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class FeedItem(Base):
    __tablename__ = 'feed'
    id = Column(Integer, primary_key=True)
    Content = Column(String(600), nullable = False)
    photo_id = Column(Integer, ForeignKey('photo.id'))
    photo = relationship(Photo)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    user_id2 = Column(Integer, ForeignKey('follower.id'))
    user2 = relationship(Follower)
   
  

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer, ForeignKey('photo.id'))
    photo = relationship(Photo)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    Comments: Column(String(500))
    CreationDate: Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
