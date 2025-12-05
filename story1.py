import streamlit as st

st.title("True Tresure")

user_name = st.text_input("Tell your name", "")

if user_name:
    st.write(f"Hello, **{user_name}**.")

if st.button("Game Start"):
    st.write(f"**{user_name}** is a trasure hunter.")
    st.write(f"To go adventure, the first thing **{user_name}** prepares is ...")
