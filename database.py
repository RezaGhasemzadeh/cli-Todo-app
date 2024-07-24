import sqlite3
from rich import print


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
                    task_content TEXT,
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

    def update(self, task_id):
        command = f"SELECT * FROM task WHERE task_id = {task_id}"
        self.cursor.execute(command)
        task = self.cursor.fetchall()
        if task:
            updated_task = input("Enter the updated task: ")
            command = f"UPDATE task SET task_content = '{updated_task}' WHERE task_id = '{task_id}'"
            self.cursor.execute(command)
            self.db.commit()
        else:
            print("\n[red]There is no such task[/red]\n")

    def get_info(self):
        command = "SELECT * FROM task"
        self.cursor.execute(command)
        info = self.cursor.fetchall()
        return info, len(info)

    def delete(self):
        pass
