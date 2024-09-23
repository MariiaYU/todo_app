FILEPATH = "/Users/mariia/PycharmProjects/(Python mega course)/TodoProject/todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def update_file(todo_list, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_list)
