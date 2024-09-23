import streamlit as st

st.title("Counter")


if 'number' not in st.session_state:
    st.session_state['number'] = 0

if st.button("Up"):
    st.session_state.number += 1

if st.button('Down'):
    st.session_state.number -= 1

if st.button("Reset"):
    st.session_state['number'] = 0
    
    
st.write(st.session_state.number)