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
                    task TEXT,
                    done TEXT
                )
                """
            )
            self.db.commit()
        finally:
            return


    def insert(self, task: str):
        tasks, tasks_len = self.get_info()
        taskid = tasks_len + 1
        done = 'no'
        self.cursor.execute(f"INSERT INTO task VALUES ('{taskid}', '{task}', '{done}')")
        self.db.commit()

    def get_info(self):
        command = "SELECT * FROM task"
        self.cursor.execute(command)
        info = self.cursor.fetchall()
        return info, len(info)

    def delete(self):
        pass
