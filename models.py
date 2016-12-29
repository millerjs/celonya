import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
engine = create_engine('sqlite:///campaign.db')
Session = sessionmaker(bind=engine)
session = Session()

class CharacterMixin(object):
    name = Column(String, primary_key=True)
    str = Column(Integer, default=0)
    con = Column(Integer, default=0)
    int = Column(Integer, default=0)
    wis = Column(Integer, default=0)
    cha = Column(Integer, default=0)
    dex = Column(Integer, default=0)

    level = Column(Integer, default=1)
    AC = Column(Integer, default=0)
    proficiency = Column(Integer, default=1)
    HP = Column(Integer, default=0)
    MHP = Column(Integer, default=0)
    speed = Column(Integer, default=0)

    race = Column(String)
    class_ = Column(String)
    background = Column(String)
    alignment = Column(String)
    age = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)

    backstory = Column(String)

    modifiers = ['str', 'con', 'int', 'wis', 'cha', 'dex']
    aux_values = ['level', 'AC', 'proficiency', 'speed', 'HP', 'MHP']
    general = ['level', 'AC', 'proficiency', 'speed', 'HP', 'MHP']

    def __repr__(self):
       return "<Character(name='%s')>" % self.name

    def __repr__(self):
       return "<%s(name='%s')>" % (self.__class__.__name__, self.name)


class Character(CharacterMixin, Base):
    __tablename__ = 'characters'


class NPC(CharacterMixin, Base):
    __tablename__ = 'npcs'


class Race(Base):
    __tablename__ = 'races'

    name = Column(String, primary_key=True)
    details = Column(String)

    def __repr__(self):
       return "<Race(name='%s')>" % self.name


class Class(Base):
    __tablename__ = 'classes'

    name = Column(String, primary_key=True)
    details = Column(String)

    def __repr__(self):
       return "<Class(name='%s')>" % self.name


class Inventories(Base):
    __tablename__ = 'inventories'

    character = Column(String, primary_key=True)
    item = Column(String, primary_key=True)
    quantity = Column(Integer)

    def __repr__(self):
       return "<InventoryItem(name='%s')>" % self.name


Base.metadata.create_all(engine)
