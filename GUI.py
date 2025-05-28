import functions
import FreeSimpleGUI as SG
import time

SG.theme("DarkPurple4")

clock = SG.Text('', key="clock")
label = SG.Text("Type in a To-Do")
input_box = SG.InputText(tooltip="enter a to-do", key="todo")
add_button = SG.Button("Add", size=10)
list_box = SG.Listbox(values=functions.get_todos(), key="items",
                      enable_events=True, size=(35, 7))     
edit_button = SG.Button("Edit")
complete_button = SG.Button("Complete")
exit_button = SG.Button("Exit")

window = SG.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%d-%m %y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['items'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['items'][0]
                new_todo = values['todo'] + '\n' #farkli bir input box ekle edit blogu icin)

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['items'].update(values=todos)
            except IndexError:
                SG.popup("Please select an item first!", font=("helvetica", 15))
        case 'Complete':
            try:
                todo_to_remove = values['items'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_remove)
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['items'].update(values=todos)
            except IndexError:
                SG.popup("Please select an item first", font=("Helvetica",15))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(values=values['todos'][0])
        case SG.WIN_CLOSED:
            break
window.close()
