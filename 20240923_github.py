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

st.title("Bild anzeige")

a = (".\GP_2\Download_1.jpg")
b = (".\GP_2\Download_2.jpg")
c = (".\GP_2\Download_3.jpg")
d = (".\GP_2\Screenshot 2024-09-09 082910.png")
e = (".\GP_2\Screenshot 2024-09-09 103707.png")
f = (".\GP_2\Screenshot 2024-09-17 190904.png")

col1, col2, col3 = st.columns (3)
col4, col5, col6 = st.columns (3)


with col1:
    st.header("Bild 1")
    st.image(a)

with col2:
    st.header("Bild 2")
    st.image(b)

with col3:
    st.header("Bild 3")
    st.image(c)

with col4:
    st.header("Bild 4")
    st.image(d)

with col5:
    st.header("Bild 5")
    st.image(e)

with col6:
    st.header("Bild 6")
    st.image(f)
    
    st.title =("change Shpend")

    st.title ("Tuerkmen")
    
    
