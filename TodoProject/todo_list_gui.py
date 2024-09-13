import FreeSimpleGUI as sg
import functions

label = sg.Text("Enter to-do: ")
input_box = sg.InputText("Enter to-do")
button = sg.Button("Add")

layout = [[label],
          [input_box, button]]

window = sg.Window("To-do List", layout=layout)
window.read()
window.close()