import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This My Todo App.")
st.text("This app is to increase your activity.")

for todo in (todos):
    st.checkbox(todo)


st.text_input(label="", placeholder="Add New Todo...", key="new_todo",
              on_change=add_todo)

