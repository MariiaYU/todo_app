import FreeSimpleGUI as sg
import functions

label = sg.Text("Enter to-do: ")
input_box = sg.InputText(key="todo")
button_add = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
button_edit = sg.Button("Edit")


layout = [[label],
          [input_box, button_add],
          [list_box, button_edit]
          ]

window = sg.Window("To-do List", layout=layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(values)
    match event:
        case "Add":
            todo = values["todo"]
            todos = functions.get_todos()
            todos.append(todo + "\n")
            functions.update_file(todos)

            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            number = todos.index(todo_to_edit)

            todos[number] = new_todo + "\n"
            functions.update_file(todos)

            window["todos"].update(values=todos)

        case sg.WIN_CLOSED:
            break

window.close()