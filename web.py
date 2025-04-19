import streamlit as st
import functions

todos = functions.read_todo()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)

st.title("my todo app")
st.subheader("this is my todo app")
st.write("this web increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[f"{todo}_{index}"]
        st.rerun()

st.text_input(label="Enter to-do:",
              placeholder="add new todo...",
              on_change=add_todo,
              key="new_todo")

