import streamlit as st
import pandas as pd
from interface import DBI

dbi = DBI('http://bugtrackerapi:8000')

bdat = dbi.get_bugs()
udat = dbi.get_users()

st.header("Bugs")

st.dataframe(bdat, 1000, 500)


if len(udat):

    ab_button = st.button("Add new bug")

    if "ab_button" not in st.session_state:
        st.session_state.ab_button = False

    if ab_button or st.session_state.ab_button:
        st.session_state.ab_button = True

    
        with st.form("add_bug_form"):
            st.write("Add bug information")
            title = st.text_input('Title')

            desc = st.text_area('Description')

            open = st.selectbox('Is open?', options=('true', 'false'))

            assign = st.selectbox(
                'Assigned to', options=tuple(udat['User ID'].values))
            submitted = st.form_submit_button("Add")
            if submitted:
                dbi.create_bug(title, desc, open, assign)
                st.session_state.ab_button = False
                st.experimental_rerun()


if len(udat) and len(bdat):

    ub_button = st.button("Update existing bug")

    if "ub_button" not in st.session_state:
        st.session_state.ub_button = False

    if ub_button or st.session_state.ub_button:
        st.session_state.ub_button = True
    
    
        choice = st.selectbox("Select a Bug ID to view", options=bdat['Bug ID'])

        with st.form("update_bug_form"):
            st.write("Update bug information")
            sel = int(choice)
            title = st.text_input(
                'Title',
                bdat.loc[bdat['Bug ID'] == sel]['Title'].values[0]
            )

            desc = st.text_area(
                'Description',
                bdat.loc[bdat['Bug ID'] == sel]['Description']. values[0]
            )

            open = st.selectbox(
                'Is open?',
                options=('true', 'false'),
                index=('True', 'False'). index(
                    str(bdat.loc[bdat['Bug ID'] == sel]['Is open?'].values[0]))
            )

            assign = st.selectbox(
                'Assigned to',
                options=tuple(udat['User ID'].values),
                index=tuple(udat['User ID'].values).index(
                    int(bdat.loc[bdat['Bug ID'] == sel]['Assigned to'].values[0]))
            )
            submitted = st.form_submit_button("Update")

            if submitted:
                dbi.update_bug(choice, title, desc, open, assign)
                st.session_state.ub_button = False
                st.experimental_rerun()
