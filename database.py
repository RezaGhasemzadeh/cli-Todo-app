import sqlite3


class Database:

    def __init__(self):
        self.db = sqlite3.connect("tasks.db")
        self.cursor = self.db.cursor()
        self.__create_table()

    def __create_table(self):
        try:
            self.cursor.execute(
                """
                CREATE TABLE task (
                    task_id INT,
                    task TEXT
                )
                """
            )
            self.db.commit()
        finally:
            return


    def insert(self, taskid: int, task: str):
        self.cursor.execute(f"INSERT INTO task VALUES ('{taskid}', '{task}')")
        self.db.commit()
        print("Inserted successfully")

    def delete(self):
        pass


