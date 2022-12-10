import sqlite3


class Database:
    def __init__(self) -> None:
        pass

    def createDatabase(self, name: str) -> None:
        self.name = name

        try:
            self.conn = sqlite3.connect(f"src/data/{self.name}")
            print("Database created successfully")
        except Exception as e:
            print("Error while creating database:", e)

        try:
            self.cur = self.conn.cursor()
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS scores(user_name text PRIMARY KEY NOT NULL, score integer NOT NULL)"
            )
            print("Table created successfully")
            self.conn.commit()

        except Exception as e:
            print("Error while creating table:", e)
