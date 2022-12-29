import sqlite3


class Database:
    def __init__(self) -> None:
        pass

    def createDatabase(self, name: str) -> None:
        self.name = name

        try:
            self.conn = sqlite3.connect(f"src/data/{self.name}")
            self.cur = self.conn.cursor()

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

    def add_user(self, user_name: str, score: int) -> None:
        self.user_name = user_name
        self.score = score

        try:
            self.cur.execute(
                "INSERT INTO scores(user_name, score) VALUES(?, ?)",
                (self.user_name, self.score),
            )
            self.conn.commit()
            print("User added successfully")
        except sqlite3.IntegrityError:
            print("User already exists")
