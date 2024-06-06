# common variables
CODEBOOK_PATH = 'data/codebook-df.xlsx'
DATA_PATH = 'data/COVID19_1_Panel_W4_new_Merge.dta'
SECTION = 'section'
QUESTION = 'question'
VAR_CODE = 'answer_code'
VAR_EXP = 'answer_explanation'
VAR_VALS = 'answer_value_mapping'
NOTES = 'notes'

# common style elements

GREEN_BUTTON = """  button {
                            background-color: green;
                            color: white;
                            border-radius: 20px;
                        } """

HIDE_MENU_STYLE = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

NAV_BOOTSTRAP = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" ' \
        'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">'


# page_0

NAV_OPTIONS_PAGE0 = """
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
            <a class="nav-link" href="http://localhost:8503/" target="_self">Download Data</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:8502/" target="_self">[placeholder]</a>
          </li>
        </ul>
      </div>
    </nav>
    """

IMAGE_URL = "data/Microbes.jpg"

MARKDOWN_TEXT = "<p>This data contains the responses of thousands of Americans, responding to hundreds of questions "\
                "asked since March 13, 2020. For more information about the data, visit "\
                "<a href='https://coronadata.us/'>CoronaData Portal</a>.</p> "\
                "<p>Contact us with questions at: <a href='CoronaDataUS@gmail.com'>CoronaDataUS@gmail.com</a> </p>"


# page_1





# page_2



# page_3