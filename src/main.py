import sqlite3

from zerocross import board, coinflip, database, menu

# initialize main menu
main_menu = menu.Menu(width=500, height=500, theme="green", appearance="system")
main_menu.display_menu(title="Zero-Cross")

# initialize database
database = database.Database()
database.createDatabase(name="player_info.db")

# Displays main menu till the name button is pressed.
while main_menu.name_button_pressed == False:
    main_menu.root.update()
else:
    if main_menu.player_name is not None:
        player_name = main_menu.player_name
        score = 0
        try:
            database.cur.execute(
                f"INSERT INTO scores(user_name,score) VALUES(?,?)", (player_name, score)
            )
        except sqlite3.IntegrityError:
            print("Username already exists")
    else:
        pass


database.cur.execute("SELECT * FROM scores")
print(database.cur.fetchall())
database.conn.commit()
database.conn.close()
