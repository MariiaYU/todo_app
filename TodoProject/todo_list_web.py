import streamlit as st
import functions

st.title("My Todo App")

todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add a new todo...")

