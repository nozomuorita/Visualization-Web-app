# modules.etc ---------------------------------------------------------------------------------------------------------------------
import os
import sys
import pandas as pd
import numpy as np
import time
from datetime import date
import re
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions

import dash
from dash import html
from dash import dcc
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff

VALID_USERNAME_PASSWORD_PAIRS = {
    'username': 'P@ssw0rd'
}
app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])
app.title = 'Visualization Web App'
app.config.suppress_callback_exceptions=True
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )