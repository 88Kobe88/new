from sql_alchemy_py.management import DB_3
from sql_alchemy_py.model import Car


class Game(DB_3):

    def insert_data_in_db(self):
        # Car(name='Audi', price=15000, car_model='Q8', release_date=2016)
        name = input('name: ')
        price = float(input('price: '))
        car_model = input('car_model ')
        release_date = input('release_date: ')
        car = Car(name=name, price=price, car_model=car_model, release_date=release_date)
        self.add_value(car=car)
        # print('add')

    def delete_values(self):
        value_id = input('Enter number of value')
        value = self.get_value_by_id(int(value_id))
        if value:
            self.delete_value(value_id)
            print(f' value ID {value_id} deleted')
        else:
            print(f' value {value_id} not found')

    def update_new_value(self):
        id = int(input('Insert Id number'))
        car_model = input('Insert car model')
        price = input('Insert price')
        self.update_value(new_car_model=car_model, new_price=price, id=id)

    def filter_new_value(self):
        new_filter = input('Enter something from car')
        self.filter_by_name(new_filter)

    def get_new_value(self):
        new_get = input('Enter id number')
        print(self.get_value_by_id(new_get))

    def run(self):
        while True:
            value = int(input('paduok skaiciu'))
            if value == 1:
                self.insert_data_in_db()
            elif value == 2:
                self.delete_values()
            elif value == 3:
                self.update_new_value()
            elif value == 4:
                self.filter_new_value()
            elif value == 5:
                self.get_new_value()
            elif value == 6:
                print('finish')
                break
            else:
                print('insert number 1 or 2')
