import streamlit as st

story1 = st.Page("story1.py", title="ストーリー１")
story2 = st.Page("story2.py", title="ストーリー２")
story3 = st.Page("story3.py", title="ストーリー３")
story4 = st.Page("story4.py", title="ストーリー４")
story5 = st.Page("story5.py", title="ストーリー５")

pg = st.navigation([story1, story2, story3, story4, story5], position='hidden')
pg.run()