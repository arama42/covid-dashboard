import streamlit as st
import pandas as pd
from streamlit_extras.stylable_container import stylable_container
from modules.constants import *


@st.cache_data
def load_survey_data():
    df = pd.read_excel(CODEBOOK_PATH)
    return df


def display_question():
    st.set_page_config(
        page_title="DisplayQuestion",
        layout="wide"
    )
    # ------------------------------------- NavBar -------------------------------------------#
    st.markdown(HIDE_MENU_STYLE, unsafe_allow_html=True)
    st.markdown(NAV_BOOTSTRAP, unsafe_allow_html=True)
    st.markdown(NAV_OPTIONS_PAGE0, unsafe_allow_html=True)

    df = load_survey_data()

    # Filter on questions
    selected_question = st.session_state.get('selected_question', '')
    filtered_data = df[df[QUESTION] == selected_question]

    with st.container():
        st.header(f"Question : {selected_question}")
        st.caption("Associated answer codes:")

        if not filtered_data.empty:
            # st.table(filtered_data[['answer_code', 'answer_explanation']])
            html = filtered_data[[VAR_CODE, VAR_EXP]].to_html(index=False, border=0)
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.write("No data available for this question.")

    # Go back
    st.write("")
    with stylable_container(
            key="back3",
            css_styles=GREEN_BUTTON,
    ):
        st.button('Go back', on_click=lambda: st.session_state.update({'page': 'page_0'}))
