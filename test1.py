import streamlit as st

st.header("st.Button")

if st.button("say hello"):
    st.write("hello")
else:
    st.write("say goodbye")
