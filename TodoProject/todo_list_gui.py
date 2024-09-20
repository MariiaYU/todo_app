import FreeSimpleGUI as sg
import functions

sg.theme("GreenMono")

label = sg.Text("Enter to-do: ")
input_box = sg.InputText(key="todo")
button_add = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
button_edit = sg.Button("Edit")
button_complete = sg.Button("Complete")
button_exit = sg.Button("Exit")
message = sg.Text()

layout = [[label],
          [input_box, button_add],
          [list_box, button_edit, button_complete],
          [button_exit]
          ]

window = sg.Window("To-do List", layout=layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todo = values["todo"].capitalize()
            todos = functions.get_todos()
            todos.append(todo + "\n")
            functions.update_file(todos)

            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                todo_to_edit = todo_to_edit
                new_todo = values["todo"].replace("\n", "")

                todos = functions.get_todos()
                number = todos.index(todo_to_edit)

                todos[number] = new_todo + "\n"
                functions.update_file(todos)

                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Select an item!", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]

                todos = functions.get_todos()
                number = todos.index(todo_to_complete)

                todos.remove(todos[number])
                functions.update_file(todos)

                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Select an item!", font=("Helvetica", 20))

        case sg.WIN_CLOSED | "Exit":
            break

window.close()