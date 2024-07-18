import sqlite3
from rich import print, box
from rich.panel import Panel
from database import Database
from rich.table import Table
# Todo ->
#  1- Implemeting the show tasks section: Done.
#  2- Implementing editing the task and pushing it into github
#


class TodoApp:

    def __init__(self):
        print(Panel("[green]Welcome to Todo app[/green]", box=box.HEAVY))
        self.db = Database()
        self.table = Table(width=120, box=box.HEAVY)
        self.initialize_table()

    def initialize_table(self):
        self.table.add_column("ID", justify="center", style="cyan")
        self.table.add_column("Task", justify="center", style="green")
        self.table.add_column("Done", justify="center", style="blue")

    def add_task(self):
        user_task = input("Enter your task: ")
        if user_task:
            try:
                self.db.insert(user_task)
                print("\n[bold green]Task added successfully[/bold green]\n")
            except:
                print("\n[bold red]There was a problem in adding task[/bold red]")
        else:
            print("\n[bold red]Empty task! try again[/bold red]\n")

    def remove_task(self):
        pass

    def show_tasks(self):
        tasks, tasks_len = self.db.get_info()
        print(Panel(f"[bold blue]There are {tasks_len} tasks available[/bold blue]"))
        for (id, task, done_inf) in tasks:
            self.table.add_row(str(id), task, done_inf)
        if self.table.rows:
            print(self.table)
        else:
            print("[red]There are no tasks yet.[/red]")

    def edit_task(self):
        pass

    def validate_user_input(self, user_input: str) -> bool:
        return user_input.isnumeric() and user_input in ['1', '2', '3', '4', '5', '6']

    def print_instructions(self):
        instructions = "\n1- Add Task\n2- Delete Task\n3- Edit Task\n4- Show Tasks\n5- Exit\n6- Mark as Done\n"
        print(instructions)

    def run(self):
        run_app = True
        while run_app:
            self.print_instructions()
            user_input = input("Enter your option: ")
            is_valid = self.validate_user_input(user_input)
            if is_valid:
                if user_input == '1':
                    self.add_task()
                elif user_input == '5':
                    run_app = False
                elif user_input == '4':
                    self.show_tasks()
            else:
                print("\n[bold red]Invalid input please try again.[/bold red]\n")
                continue


if __name__ == "__main__":
    app = TodoApp()
    app.run()
