import sqlite3

class DB_2:

    def __init__(self, url='lection_db.db'):
        self.url = url
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()

    def __run_sql_query(self, sql_query):
        self.cursor.execute(sql_query)
        self.connection.commit()

    def create_table(self, data):
        table_name = data['table_name']
        sql_middle = ''
        for key, value in data['columns'].items():
            sql_middle += f'{key} {value}, '

        sql_query = f"""CREATE TABLE IF NOT EXISTS {table_name} 
        ({sql_middle[:-2]});"""

        self.__run_sql_query(sql_query=sql_query)

    def insert_values_to_table(self, data):

        for lecture in data:
            sql_query = f"""
            INSERT INTO lecture(lecture_name, teacher, hours)
            VALUES ("{lecture[0]}", "{lecture[1]}", {lecture[2]});
            """
            # print(sql_query)
            self.__run_sql_query(sql_query=sql_query)

    def count_hours(self, hours=50):
        sql_query = f"""
        SELECT * 
        FROM lecture
        WHERE hours > {hours};
"""
        result = self.cursor.execute(sql_query)
        print(result.fetchall())

    def update_rows(self, data):
        sql_query = f"""
        UPDATE lecture SET lecture_name = "{data['new_value']}"
        WHERE lecture_name = "{data['old_value']}"
        """
        self.__run_sql_query(sql_query=sql_query)

    def delete_rows(self, data):
        sql_query = f"""
        DELETE FROM lecture
        WHERE """
        for key, value in data.items():
            sql_query += f'{key}="{value}" AND '

        sql_query = sql_query[:-5] + ';'
        self.__run_sql_query(sql_query=sql_query)







