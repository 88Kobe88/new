from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_alchemy_py.model import Car

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()

class DB_3():


    def __init__(self):
        self.session = Session()

    def add_value(self, car):
        session.add(car)
        session.commit()

    def get_value_by_id(self, id):
        value = self.session.query(Car).get(id)
        return value

    def filter_by_name(self, name):
        value = self.session.query(Car).filter_by(name=name).all()
        print(value)

    def update_value(self, id, new_car_model, new_price):
        value = self.session.query(Car).get(id)
        value.car_model = new_car_model
        value.price = new_price
        self.session.commit()

    def delete_value(self, id):
        value = self.session.query(Car).get(id)
        self.session.delete(value)
        self.session.commit()

