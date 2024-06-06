import streamlit as st
import pandas as pd
from streamlit_extras.stylable_container import stylable_container
from modules.constants import *


@st.cache_data()
def load_survey_data():
    df = pd.read_stata(DATA_PATH, convert_dates=False)
    return df


def display_summary():
    st.set_page_config(
        page_title="DisplayVariable",
        layout="wide"
    )
    # ------------------------------------- NavBar -------------------------------------------#

    st.markdown(HIDE_MENU_STYLE, unsafe_allow_html=True)
    st.markdown(NAV_BOOTSTRAP, unsafe_allow_html=True)
    st.markdown(NAV_OPTIONS_PAGE0, unsafe_allow_html=True)

    # ------------------------------------- Header -------------------------------------------#

    page1 = st.container(border=True)
    page1 = stylable_container(key="page1",
                               css_styles=""" {box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 25px;} """)

    cols = page1.columns([1, 1, 2, 1, 1])
    cols[2].header(f"Variable : {st.session_state['selected_code']}", anchor='section-1',
                   help='Variable and associated details.')
    page1.divider()

    # ------------------------------------- Details -------------------------------------------#
    data = {
        "Category": ["Associated Section", "Associated Questions", "Variable Explanation", "Variable Values", "Notes"],
        "Details": [
            st.session_state.get('selected_section', 'Not Available'),
            st.session_state.get('selected_question', 'Not Available'),
            st.session_state.get('selected_code_exp', 'Not Available'),
            st.session_state.get('selected_mapping', 'Not Available'),
            st.session_state.get('selected_notes', 'Not Available')
        ]
    }
    table_df = pd.DataFrame(data)
    cols = page1.columns([0.5, 5, 0.5])
    cols[1].caption(f"Associated details for {st.session_state['selected_code']}")
    cols[1].table(table_df)

    # ------------------------------------- statistics -------------------------------------------#
    df = load_survey_data()

    selected_code = st.session_state['selected_code']
    cols[1].caption(f"Statistics for {selected_code}")
    if selected_code in df.columns:
        cols[1].write(df[selected_code].describe())
    else:
        cols[1].error("Data for the selected answer code is not available.")

    page1.markdown("#")

    with stylable_container(
            key="back1",
            css_styles=GREEN_BUTTON,
    ):
        if st.button('Go back', key='back1'):
            st.session_state['page'] = 'page_0'
