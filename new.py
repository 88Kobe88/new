import sqlite3

class DB:

    def __init__(self, url='new_db'):
        self.url = url

    def create_table(self):
        connection = sqlite3.connect('new.db')
        cursor = connection.cursor()
        create_cars_table = """
        create table if not exists cars(
        car_name text,
        car_model text,
        car_year integer
        );
        """

        cursor.execute(create_cars_table)
        connection.commit()
        connection.close()

    def insert_values(self):
        with sqlite3.connect('new.db') as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO cars VALUES('Ford', 'Mustang', '1985')")
            cursor.execute("INSERT INTO cars VALUES('Dodge', 'Journey', '2014')")
            cursor.execute("INSERT INTO cars VALUES('BMW', 'X6', '2020')")

    def delete_rows(self, car_model):
        with sqlite3.connect('new.db') as connection:
            cursor = connection.cursor()
            cursor.execute(f"DELETE from cars WHERE car_model = 'Mustang'")

db=DB()
db.create_table()
db.insert_values()










