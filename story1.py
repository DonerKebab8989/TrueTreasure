import streamlit as st

st.title("True Tresure")

user_name = st.text_input("Tell your name", "")

if user_name:
    st.write(f"Hello, **{user_name}**.")

st.page_link("story2.py", label="New Game")