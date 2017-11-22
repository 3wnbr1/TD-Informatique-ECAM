#! /Users/ewen/anaconda3/bin/python
# coding: utf-8

"""Class for nitron.db ."""


from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BottomEye(Base):
    __tablename__ = 'BottomEye'
    Id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    LengthCor = Column(String(250))


class TopEye(Base):
    __tablename__ = 'TopEye'
    Id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    LengthCor = Column(String(250))


class Bumpstop(Base):
    __tablename__ = 'Bumpstop'
    Id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Length = Column(Integer)
    Compressed = Column(Integer)


class Packers(Base):
    __tablename__ = 'Packers'
    Id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Length = Column(Float)


class Rod(Base):
    __tablename__ = "Rod"
    Id = Column(Integer, primary_key=True)
    length = Column(Integer)


class Tube(Base):
    __tablename__ = "Tube"
    Id = Column(Integer, primary_key=True)
    length = Column(Integer)


class Stroke(Base):
    __tablename__ = "Stroke"
    Id = Column(Integer, primary_key=True)
    Length = Column(Integer)
