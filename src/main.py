# To-Do --------------------------------------------------------------------------------------------------------------------------
# 1. Download png ボタン作成
# 2. Executionタブの作成
# 3. Judgeタブの作成

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
import dash_auth
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff

from func import *
from app import app
from layout import layout
import callback

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True, port=1237)