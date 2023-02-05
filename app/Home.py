import streamlit as st
import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

with open('./app/md/intro.md') as f:
    intro = f.read()

st.title('Simple Bug Tracker :bug: :ant:')

st.markdown(intro)
