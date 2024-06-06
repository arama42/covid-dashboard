import pandas as pd
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from modules.helper import validate
from modules.constants import *


@st.cache_data
def load_metadata():
    return pd.read_excel(CODEBOOK_PATH, engine='openpyxl')


def home_page():
    # ----------------------------------- Page Settings ------------------------------------------ #
    st.set_page_config(
        page_title="CoronaData",
        layout="wide"
    )

    # --------------------------------------- CSS style ------------------------------------------ #
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    local_css("style.css")

    # ----------------------------------------- NavBar ----------------------------------------------#
    st.markdown(HIDE_MENU_STYLE, unsafe_allow_html=True)
    st.markdown(NAV_BOOTSTRAP, unsafe_allow_html=True)
    st.markdown(NAV_OPTIONS_PAGE0, unsafe_allow_html=True)

    # ----------------------------------- Main title ------------------------------------------ #
    page0 = stylable_container(key="page0",
                               css_styles="""{box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 25px;}""")

    page0.markdown("<h1 style='text-align: center;'>CoronaData U.S.</h1>", unsafe_allow_html=True)
    page0.markdown("<p style='text-align: center;'> by <a href='https://www.bethredbird.com/'>Beth Redbird</a></p>",
                   unsafe_allow_html=True)

    # ----------------------------------- Image ------------------------------------------ #
    cols = page0.columns([1, 2, 1])
    cols[1].image(IMAGE_URL, caption='', width=700)
    page0.markdown("#")

    # ----------------------------------- Data ------------------------------------------ #
    metadata = load_metadata()

    # ----------------------------------- Tab1 ------------------------------------------ #
    tab1, tab2 = st.tabs(["Variables", "Questions"])
    with tab1:
        col1, col2 = st.columns(2)

        # Dropdown section
        with col1:
            section_options = ["All"] + sorted(metadata['section'].unique().tolist())
            selected_section = st.selectbox("Select a Section:", section_options, key='vselect')

        # Search variable
        with col2:
            search_query = st.text_input("Search for a variable: 🔍", "")

        # Filter data on search query
        if search_query:
            filtered_data = metadata[metadata[VAR_CODE].str.contains(search_query, case=False)]
        else:
            filtered_data = metadata

        # Apply section filter if a specific section is selected
        if selected_section != "All":
            filtered_data = filtered_data[filtered_data[SECTION] == selected_section]

        # ----------------------------------- Paginate Data -----------------------------------------#
        items_per_page = 20
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 0

        start_index = st.session_state.current_page * items_per_page
        end_index = start_index + items_per_page
        page_data = filtered_data[start_index:end_index]

        # Display variables with associated questions as dropdowns
        for index, row in page_data.iterrows():
            with st.expander(f"{row[VAR_CODE]}"):
                st.write(f"Question: {row[QUESTION] if row[QUESTION] else 'None'}")
                if st.button('View More', key=row[VAR_CODE]):
                    st.session_state['selected_code'] = row[VAR_CODE]
                    st.session_state['selected_code_exp'] = validate(row[VAR_EXP])
                    st.session_state['selected_question'] = row[QUESTION]
                    st.session_state['selected_section'] = row[SECTION]
                    st.session_state['selected_notes'] = validate(row[NOTES])
                    st.session_state['selected_mapping'] = row[VAR_VALS]
                    st.session_state['page'] = 'page_1'

        # ----------------------------------- Page buttons ------------------------------------- #
        col1, col2 = st.columns(2)
        with col1:
            with stylable_container(
                    key="prev0",
                    css_styles=GREEN_BUTTON,
            ):
                if st.button("Previous"):
                    if st.session_state.current_page > 0:
                        st.session_state.current_page -= 1
        with col2:
            with stylable_container(
                    key="next0",
                    css_styles=GREEN_BUTTON,
            ):
                if st.button("Next"):
                    if end_index < len(filtered_data):
                        st.session_state.current_page += 1

    # ---------------------------------------- Tab 2 ------------------------------------------- #
    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            section_options = ["All"] + sorted(metadata[SECTION].unique().tolist())
            selected_section = st.selectbox("Select a Section:", section_options, key='qselect')
        with col2:
            search_query = st.text_input("Search for a question: 🔍")

        if search_query:
            question_data = metadata[metadata[QUESTION].str.contains(search_query, case=False)]
        else:
            question_data = metadata

        if selected_section != "All":
            question_data = question_data[question_data[SECTION] == selected_section]

        # Group data by question
        grouped_data = question_data.groupby(QUESTION)[VAR_CODE].apply(list).reset_index()

        # Pagination
        items_per_page = 20
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 0

        start_index = st.session_state.current_page * items_per_page
        end_index = start_index + items_per_page
        page_data = grouped_data.iloc[start_index:end_index]

        for index, row in page_data.iterrows():
            with st.expander(f"{row[QUESTION]}"):
                if st.button('View More', key=row[QUESTION]):
                    st.session_state['selected_question'] = row[QUESTION]
                    st.session_state['page'] = 'page_3'

        # nav buttons
        col1, col2 = st.columns(2)
        with col1:
            with stylable_container(
                    key="prev01",
                    css_styles=GREEN_BUTTON,
            ):
                if st.button("Previous", key="prev01"):
                    if st.session_state.current_page > 0:
                        st.session_state.current_page -= 1

        with col2:
            with stylable_container(
                    key="next01",
                    css_styles=GREEN_BUTTON,
            ):
                if st.button("Next", key="next01"):
                    if end_index < len(grouped_data):
                        st.session_state.current_page += 1

    # -----------------------------------  Disclaimer  ----------------------------------- #
    # with bottom():
    st.divider()
    st.markdown(MARKDOWN_TEXT, unsafe_allow_html=True)
