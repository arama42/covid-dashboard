import streamlit as st
import pandas as pd
import json
from modules.helper import todict


@st.cache_data()
def load_survey_data():
    df = pd.read_stata('data/COVID19_1_Panel_W4_new_Merge.dta', convert_dates=False)
    return df


def display_summary():
    # ------------------------------------- NavBar -------------------------------------------#
    hide_menu_style = """
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)

    st.markdown("""
        <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #2F4F4F;">
          <a class="navbar-brand" href="https://www.ipr.northwestern.edu/who-we-are/faculty-experts/redbird.html" target="_blank">Redbird Lab</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item active">
                <a class="nav-link disabled" href="http://localhost:8502/" target="_self">Variable Detail<span class="sr-only">(current)</span></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="http://localhost:8502/" target="_self">[placeholder]</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="http://localhost:8502/" target="_self">[placeholder]</a>
              </li>
            </ul>
          </div>
        </nav>
        """, unsafe_allow_html=True)

    st.title(f"Variable : {st.session_state['selected_code']}")
    st.text(f"Associated Section : {st.session_state['selected_section']}")
    st.text(f"Associated Questions : {st.session_state['selected_question']}")
    st.text(f"Variable Explanation : {st.session_state['selected_code_exp']}")

    df = load_survey_data()
    selected_code = st.session_state['selected_code']

    if selected_code in df.columns:
        st.write(f"Statistics for {selected_code}")
        st.write(df[selected_code].describe())
    else:
        st.error("Data for the selected answer code is not available.")

    st.text(f"Value maps : ")
    mapping = st.session_state['selected_mapping']
    if isinstance(mapping, dict):
        for key, val in mapping.items():
            print(key, val)
    else:
        st.text(mapping)

    # st.text(f"Value maps : {st.session_state['selected_mapping']}")
    st.text(f"Notes : {st.session_state['selected_notes']}")

    if st.button('Go back'):
        st.session_state['page'] = 'home'
