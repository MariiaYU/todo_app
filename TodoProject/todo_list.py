from functions import get_todos, update_file
import time

today_day = time.strftime("%B %d, %Y, %I%p")
print(today_day)


while True:
    user_action = input("Enter 'add', 'show', 'edit', 'delete' or 'exit': ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        update_file(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        new_todos = [item.strip("\n") for item in todos]
        for index, x in enumerate(new_todos):
            print(f"{index+1}. {x.title()}")

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()
            number = int(user_action[5:])
            if len(todos) >= number > 0:
                edit_todo = input("Type a new todo: ") + "\n"
                todos[number-1] = edit_todo
                update_file(todos)
            else:
                print("No item found!")
        except (ValueError, IndexError):
            print("You must put a correct number.")
            continue

    elif user_action.startswith("delete"):
        try:
            delete_element = int(user_action[7:])
            todos = get_todos()
            todos.remove(todos[delete_element-1])
            update_file(todos)
        except (ValueError, IndexError):
            print("You must put a correct number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("The command not valid.")




