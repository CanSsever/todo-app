import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This My Todo App.")
st.text("This app is to increase your activity.")

for i, todo in enumerate(todos):
    st.checkbox(todo, key=f"checkbox_{i}")


st.text_input(label="", placeholder="Add New Todo...")
