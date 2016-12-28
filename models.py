import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
engine = create_engine('sqlite:///campaign.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Character(Base):
    __tablename__ = 'characters'

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

    modifiers = ['str', 'con', 'int', 'wis', 'cha', 'dex']
    aux_values = ['level', 'AC', 'proficiency', 'speed', 'HP', 'MHP']

    def __repr__(self):
       return "<Character(name='%s')>" % self.name
