import FreeSimpleGUI as sg
import functions

label = sg.Text("Enter to-do: ")
input_box = sg.InputText(key="todo")
button = sg.Button("Add")

layout = [[label],
          [input_box, button]]

window = sg.Window("To-do List", layout=layout, font=("Helvetica", 20))


while True:
    event, values = window.read()

    match event:
        case "Add":
            todo = values["todo"]
            todos = functions.get_todos()
            todos.append(todo + "\n")
            functions.update_file(todos)
        case sg.WIN_CLOSED():
            break

window.close()