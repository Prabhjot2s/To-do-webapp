import streamlit as st
import function


file = function.openfile()

def add_todo():
    value = st.session_state["Input"]+"\n"
    file.append(value)
    function.writeline(file)


st.title("Todo APP")





for index,val in enumerate(file):
    checkbox=st.checkbox(val, key=val)
    if checkbox:
        file.pop(index)
        function.writeline(file)
        del st.session_state[val]
        st.experimental_rerun()



st.text_input('', placeholder="Add the todo ", on_change=add_todo, key="Input")
