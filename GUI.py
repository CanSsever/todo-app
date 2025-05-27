import functions
import FreeSimpleGUI as SG

label = SG.Text("Type in a To-Do")
input_box = SG.InputText(tooltip="enter a to-do", key="todo")
add_button = SG.Button("Add")

window = SG.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case SG.WIN_CLOSED:
            break
window.close()
