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
        return "<%s(name='%s')>" % (self.__class__.__name__, self.name)


class Character(CharacterMixin, Base):
    __tablename__ = 'characters'


class NPC(CharacterMixin, Base):
    __tablename__ = 'npcs'


class MonsterMixin(object):
    name = Column(String, primary_key=True)
    str = Column(Integer, default=0)
    con = Column(Integer, default=0)
    int = Column(Integer, default=0)
    wis = Column(Integer, default=0)
    cha = Column(Integer, default=0)
    dex = Column(Integer, default=0)
    HP = Column(Integer)
    AC = Column(Integer)
    speed = Column(String)

    size = Column(String)
    type = Column(String)
    subtype = Column(String)
    alignment = Column(String)
    hit_dice = Column(String)
    stealth = Column(Integer)
    damage_vulnerabilities = Column(String)
    damage_resistances = Column(String)
    damage_immunities = Column(String)
    condition_immunities = Column(String)
    senses = Column(String)
    languages = Column(String)
    challenge_rating = Column(String)
    special_abilities = Column(String)
    actions = Column(String)

    modifiers = ['str', 'con', 'int', 'wis', 'cha', 'dex']
    aux_values = ['AC', 'speed', 'HP', 'MHP']
    general = ['AC', 'speed', 'HP', 'MHP']

    def __repr__(self):
        return "<%s(name='%s')>" % (self.__class__.__name__, self.name)


class Monster(MonsterMixin, Base):
    __tablename__ = 'monsters'


class MonsterInstance(MonsterMixin, Base):
    __tablename__ = 'monster_instances'

    monster_type = Column(String)


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


class InventoryItem(Base):
    __tablename__ = 'inventories'

    character = Column(String, primary_key=True)
    item = Column(String, primary_key=True)
    quantity = Column(Integer, default=1)

    def __repr__(self):
        return "<InventoryItem(name='%s')>" % self.item


class Item(Base):
    __tablename__ = 'items'

    name = Column(String, primary_key=True)
    description = Column(String)
    category = Column(String)
    ac = Column(String)
    weight = Column(String)
    cost = Column(String)
    strength = Column(String)
    stealth = Column(String)
    damage = Column(String)
    properties = Column(String)

    def __repr__(self):
        return "<Item(name='%s')>" % self.name


class Encounter(Base):
    __tablename__ = 'encounters'

    name = Column(String, primary_key=True)
    description = Column(String)

    def __repr__(self):
        return "<Encounter(name='%s')>" % self.name

Base.metadata.create_all(engine)
