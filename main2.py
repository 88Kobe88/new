from lection import DB_2

table = {
    'table_name': 'lecture',
    'columns':{
    'lecture_name' : 'text',
    'teacher' : 'text',
    'hours' : 'integer',
    }
}

lecture = [
    ('Vadyba', 'Domantas', '40'),
    ('Python', 'Donatas', '80'),
    ('Java', 'Tomas', '80'),
]
data = {
    'old_value': ('Python'),
    'new_value': ('Python programavimas'),
}

delete_data = {
    'lecture_name': 'Java'
}

db_2=DB_2()
db_2.create_table(data=table)
db_2.insert_values_to_table(lecture)
db_2.count_hours()
db_2.update_rows(data)
db_2.delete_rows(data=delete_data)