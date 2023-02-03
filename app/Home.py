import streamlit as st

with open('./app/md/intro.md') as f:
    intro = f.read()

st.title('Simple Bug Tracker :bug: :ant:')

st.markdown(intro)
