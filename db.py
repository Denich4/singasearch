from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String

engine = create_engine("sqlite:///prices.db")

class Base(DeclarativeBase): pass

class YuraPrice(Base):
    __tablename__ = "yura_prices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    picture = Column(String)
    link = Column(String)


class SingaPrice(Base):
    __tablename__ = "singa_prices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    picture = Column(String)
    link = Column(String)

Base.metadata.create_all(bind=engine)