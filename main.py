import sqlite3
from rich import print, box
from rich.panel import Panel


class TodoApp:

    def __init__(self):
        print(Panel("[green]Welcome to Todo app[/green]", box=box.HEAVY))
        self.database = sqlite3.connect("tasks.db")

    def add_task(self):
        pass

    def remove_task(self):
        pass

    def edit_task(self):
        pass

    def validate_user_input(self, user_input: int) -> bool:
        return user_input.isnumeric() and user_input in ['1', '2', '3', '4', '5']

    def print_instructions(self):
        instructions = "\n1- Add Task\n2- Delete Task\n3- Edit Task\n4- Show Tasks\n5- Exit\n"
        print(instructions)

    def run(self):
        run_app = True
        while run_app:
            self.print_instructions()
            user_input = input("Enter your option: ")
            is_valid = self.validate_user_input(user_input)
            if is_valid:
                pass
            else:
                print("\n[bold red]Invalid input please try again.[/bold red]\n")
                continue


if __name__ == "__main__":
    app = TodoApp()
    app.run()

