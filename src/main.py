import sqlite3

from zerocross import board, coinflip, database, menu

# initialize main menu
main_menu = menu.Menu(width=500, height=500, theme="green", appearance="system")
main_menu.display_menu(title="Zero-Cross")

# initialize database
database = database.Database()
database.createDatabase(name="player_info.db")

# initialize board
board = board.Board()

# Displays main menu till the name button is pressed.
while main_menu.name_button_pressed == False:
    main_menu.root.update()
else:
    if main_menu.player_name is not None:
        database.add_user(user_name=main_menu.player_name, score=0)
    else:
        pass

board.display_board()


database.cur.execute("SELECT * FROM scores")
print(database.cur.fetchall())
database.conn.commit()
database.conn.close()
