import FreeSimpleGUI

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def update_file(todo_list, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_list)
