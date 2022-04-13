import streamlit as st

if 'increment' not in st.session_state:
    st.session_state.increment = 0
    
button = st.button("Incrementer")

if button:
    st.session_state.increment += 1
    
st.write('Increment', st.session_state.increment)