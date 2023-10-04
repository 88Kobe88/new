from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///projektai.db')
Base = declarative_base()


class Car(Base):
    __tablename__ = 'Car'
    id = Column(Integer, primary_key=True)
    name = Column("Car_name", String)
    price = Column("Price", Float)
    car_model = Column("Car_model", String)
    release_date = Column("Release_date", Integer)
    created_date = Column("Created_date", DateTime, default=datetime.utcnow)

    def __init__(self, name, price, car_model, release_date):
        self.name = name
        self.price = price
        self.car_model = car_model
        self.release_date = release_date

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date} {self.car_model} {self.release_date}"


Base.metadata.create_all(engine)
