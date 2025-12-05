import streamlit as st

st.title("True Tresure")

user_name = st.text_input("Tell your name", "")

if user_name:
    st.write(f"Hello, **{user_name}**.")

if st.button("Game Start"):
    st.write(f"**{user_name}** is a trasure hunter.")
    q1 = st.radio(
        f"To go on an adventure, the first thing **{user_name}** prepares is ...",
        ["Treasure map :🗺️:", "Companions :🧑‍🤝‍🧑:", "Equipments :🔦:", "Provisions :🍎:"],
        index=None
    )
    if q1 is not None:
        st.page_link("story2.py", label="Next")
    else:
        st.write("Choose and click")