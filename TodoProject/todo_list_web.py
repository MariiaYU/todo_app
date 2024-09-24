import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.update_file(todos)

st.title("My Todo App")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.update_file(todos)
        del st.session_state[item]
        st.rerun()


st.text_input(label="Enter a todo:", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")


