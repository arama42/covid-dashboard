import pandas as pd
import streamlit as st
from modules.data_download import filter_dataframe
from streamlit_extras.stylable_container import stylable_container

@st.cache_data()
def load_survey_data():
    df = pd.read_stata('data/COVID19_1_Panel_W4_new_Merge.dta', convert_dates=False)
    return df


def download_page():
    st.set_page_config(
        page_title="DataDownload",
        layout="wide"
    )
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
                  <li class="nav-item ">
                    <a class="nav-link " href="http://localhost:8502/" target="_self">Variable Detail</a>
                  </li>
                  <li class="nav-item active">
                    <a class="nav-link disabled" href="http://localhost:8503/" target="_self">Download Data<span class="sr-only">(current)</span></a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="http://localhost:8502/" target="_self">[placeholder]</a>
                  </li>
                </ul>
              </div>
            </nav>
            """, unsafe_allow_html=True)

    # ------------------------------------- SideBar -------------------------------------------#
    side_bar = """
     <style>
     /* The whole sidebar */
     .css-1lcbmhc.e1fqkh3o0{
     margin-top: 3.8rem;
     }

     /* The display arrow */
     .css-sg054d.e1fqkh3o3 {
     margin-top: 5rem;
     }
     </style> 
     """
    st.markdown(side_bar, unsafe_allow_html=True)

    # st.title("Download Data")
    # st.write(
    #     """Options to download full data OR filter on columns and download selected data.
    #     """
    # )

    # ------------------------------------- Title -------------------------------------------#
    page2 = stylable_container(key="Page2", css_styles=""" {box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 15px;} """)
    st.header("Download Data", anchor='section-3',
              help='Options to download full data OR use the filters to determine what data you need.',
              divider='gray')

    # ------------------------------------- Data -------------------------------------------#
    df = load_survey_data()
    st.dataframe(filter_dataframe(df), width=700, height=400)

    with stylable_container(
            key="green_button",
            css_styles="""
            button {
                background-color: green;
                color: white;
                border-radius: 20px;
            }
            """,
    ):
        if st.button('Go back'):
            st.session_state['page'] = 'page_0'
