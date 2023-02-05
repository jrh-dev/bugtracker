import streamlit as st
import pandas as pd
from interface import DBI
import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

dbi = DBI('http://bugtrackerapi:8000')

bdat = dbi.get_bugs()
udat = dbi.get_users()

st.header("Users")

st.dataframe(udat, 1000, 500)

ua_button = st.button("Add new user")

if "ua_button" not in st.session_state:
    st.session_state.ua_button = False

if ua_button or st.session_state.ua_button:
    st.session_state.ua_button = True

    with st.form("add_user_form"):
        st.write("Add user information")
        first_name = st.text_input('First Name')

        last_name = st.text_input('Last Name')

        submitted = st.form_submit_button("Add")
        if submitted:
            dbi.create_user(first_name, last_name)
            st.session_state.ua_button = False
            st.experimental_rerun()

if len(udat):
    uu_button = st.button("Update existing user")

    if "uu_button" not in st.session_state:
        st.session_state.uu_button = False

    if uu_button or st.session_state.uu_button:
        st.session_state.uu_button = True
            
        choice = st.selectbox("Select a User ID to view", options=udat['User ID'])
        sel = int(choice)

        with st.form("update_user_form"):
            st.write("Update user information")

            first_name = st.text_input(
                'First Name',
                udat.loc[udat['User ID'] == sel]['First Name'].values[0]
            )

            last_name = st.text_input(
                'Last Name',
                udat.loc[udat['User ID'] == sel]['Last Name'].values[0]
            )
            submitted = st.form_submit_button("Update")

            if submitted:
                dbi.update_user(sel, first_name, last_name)
                st.session_state.uu_button = False
                st.experimental_rerun()
