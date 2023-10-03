from sql_alchemy_py.model import Car
from sql_alchemy_py.management import DB_3
from datetime import datetime

db = DB_3()
# Car(name='Volvo', price=10000, car_model='XC90', release_date=2005, created_date=datetime.today())
# Car(name='Dodge', price=9500, car_model='Journey', release_date=2014, created_date=datetime.today())
# Car(name='Audi', price=15000, car_model='Q8', release_date=2016
car = Car(name='Jeep', price=11000, car_model='Grand_Sheroke', release_date=2012, created_date=datetime.today())

# db.add_value(car)
# db.get_value_by_id(3)
# db.filter_by_name('Dodge')
# db.update_value(id=3, new_car_model='Q7', new_price=17000)
db.delete_value(id=2)
