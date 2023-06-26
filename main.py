import streamlit as st
import function

st.title("Todo APP")


def add_todo():
    value = st.session_state["Input"]
    file.append(value + '\n')
    function.writeline(file)


def show_list(file):
    for files in file:
        st.checkbox(files, key=files)


file = list(function.openfile())

show_list(file)

for val in file:
    match st.session_state[val]:
        case True:
            file.remove(val)
            function.writeline(file)
            del st.session_state[val]
            st.experimental_rerun()
        case False:
            continue

st.text_input('', placeholder="Add the todo ", on_change=add_todo, key="Input")
