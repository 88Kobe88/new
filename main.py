from game.game import Game
from sql_alchemy_py.management import DB_3

game=Game()
game.run()
game.insert_data_in_db()
game.delete_values()