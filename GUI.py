import functions
import FreeSimpleGUI as SG

label = SG.Text("Type in a To-Do")
input_box = SG.InputText(tooltip="enter a to-do", key="todo")
add_button = SG.Button("Add")
list_box = SG.Listbox(values=functions.get_todos(), key="items",
                      enable_events=True, size=(35, 7))
edit_button = SG.Button("Edit")
complete_button = SG.Button("Complete")
exit_button = SG.Button("Exit")

window = SG.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

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
            window['items'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['items'][0]
            new_todo = values['todo'] + '\n' #farkli bir input box ekle edit blogu icin)

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['items'].update(values=todos)

        case 'Complete':
            todo_to_remove = values['items'][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_remove)
            todos.remove(todo_to_remove)
            functions.write_todos(todos)
            window['items'].update(values=todos)
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(values=values['todos'][0])
        case SG.WIN_CLOSED:
            break
window.close()
