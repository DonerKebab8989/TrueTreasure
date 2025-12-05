import streamlit as st

story1 = st.Page("story1.py", title="ストーリー１")
story2 = st.Page("story2.py", title="ストーリー２")
story3 = st.Page("story3.py", title="ストーリー３")
story4 = st.Page("story4.py", title="ストーリー４")
story5 = st.Page("story5.py", title="ストーリー５")

st.title("True Treasure")

user_name = st.text_input("Tell your name", "")

if user_name:
    st.write(f"Hello, **{user_name}** .")

st.page_link("story1.py", label="New Game", icon="🆕")