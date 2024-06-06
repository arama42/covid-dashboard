import pandas as pd
import streamlit as st
from modules.data_download import filter_dataframe

from modules.data_summary import display_summary
from dashboard import main_page


@st.cache_data()
def load_survey_data():
    df = pd.read_stata('../data/COVID19_1_Panel_W4_new_Merge.dta', convert_dates=False)
    return df


def download_page():
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
                    <a class="nav-link disabled" href="http://localhost:8502/" target="_self">Variable Detail</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="http://localhost:8503/" target="_self">Download Data<span class="sr-only">(current)</span></a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="http://localhost:8502/" target="_self">[placeholder]</a>
                  </li>
                </ul>
              </div>
            </nav>
            """, unsafe_allow_html=True)

    st.title("Download Data")
    st.write(
        """Options to download full data OR filter on columns and download selected data.
        """
    )

    df = load_survey_data()
    st.dataframe(filter_dataframe(df))

    if st.button('Go back'):
        st.session_state['page'] = 'home'


def download():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'download'

    if st.session_state['page'] == 'download':
        download_page()
    elif st.session_state['page'] == 'home':
        main_page()
    elif st.session_state['page'] == 'details':
        display_summary()


if __name__ == "__main__":
    download()


# # Contents of ~/my_app/streamlit_app.py
# import streamlit as st
# def main_page():
#     st.markdown("# Main page 🎈")
#     st.sidebar.markdown("# Main page 🎈")
# def page2():
#     st.markdown("# Page 2 ❄️")
#     st.sidebar.markdown("# Page 2 ❄️")
# def page3():
#     st.markdown("# Page 3 🎉")
#     st.sidebar.markdown("# Page 3 🎉")
# page_names_to_funcs = {
#     "Main Page": main_page,
#     "Page 2": page2,
#     "Page 3": page3,
# }
# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()
