import pandas as pd
import streamlit as st
from pages.page0 import home_page
from pages.page1 import display_summary
from pages.page2 import download_page
from pages.page3 import display_question


def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'page_2'

    if st.session_state['page'] == 'page_2':
        download_page()
    elif st.session_state['page'] == 'page_0':
        home_page()
    elif st.session_state['page'] == 'page_1':
        display_summary()
    elif st.session_state['page'] == 'page_3':
        display_question()


if __name__ == "__main__":
    main()

