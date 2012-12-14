# -*- coding: utf-8 -*-
__author__ = 'ewok'

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from db import Base
from config import IMAGES_PATH
from utils import generate_and_save_thumbnail

class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    percent = Column(Integer, unique=False)

    def __init__(self, title, percent=0):
        self.title = title
        self.percent = percent

    def __repr__(self):
        return '<Skill %r complete on %r percent>' % (self.title, self.percent)


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    description = Column(String(255), unique=False)
    logo = Column(String(100), unique=False)
    link = Column(String(100), unique=False)
    project = relationship('Project')

    def __init__(self, title, description='', logo='/no-logo.png', link='http://'):
        self.title = title
        self.description = description
        self.logo = logo
        self.link = link

    def __repr__(self):
        return '<Company %r>' % self.title


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    description = Column(String(255), unique=False)
    project = relationship('Project')

    def __init__(self, title, description=''):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Category %r>' % self.title


class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    description = Column(String(255), unique=False)
    logo = Column(String(100), unique=False)
    link = Column(String(100), unique=False)
    client_id = Column(Integer, ForeignKey('client.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

    client = relationship(Client, primaryjoin=client_id == Client.id)

    def get_thumb(self):
        thumb_name = 'no-logo.png'

        if self.logo:
            thumb_name = generate_and_save_thumbnail(self.logo, 200, 200) or thumb_name

        return thumb_name

    thumb = property(get_thumb)

    def __init__(self, title, description='', logo='no-logo.png', link='http://', client_id=0, category_id=0):
        self.title = title
        self.description = description
        self.logo = logo
        self.link = link
        self.client_id = client_id
        self.category_id = category_id

    def __repr__(self):
        return '<Category %r>' % self.title


class Info(Base):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    value = Column(Text, unique=False)

    def __init__(self, title=None, value=""):
        self.title = title
        self.value = value

    def __repr__(self):
        return '<Param %r>' % self.title

    @staticmethod
    def get_param(title):
        value = Info.query.filter(Info.title == title).first()
        return value.value

