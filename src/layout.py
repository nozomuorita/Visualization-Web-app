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

from func import *
import components.performance as perf
import components.data as data
import components.execution as execution
import components.judge as judge
import components.sidebar as sidebar
import components.help as help_tab
import components.footer as footer

sidebar = sidebar.sidebar
tab1_content = perf.tab1_content
tab2_content = data.tab2_content
tab3_content = execution.tab3_content
tab4_content = judge.tab4_content
help_content = help_tab.help
footer = footer.footer

tabs = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab(
                    "Performance",
                    icon=DashIconify(icon="streamline:money-graph-bar-increase-up-product-performance-increase-arrow-graph-business-chart"),
                    value="performance",
                    className='tab',
                ),
                dmc.Tab(
                    "Data",
                    icon=DashIconify(icon="mdi:graph-line"),
                    value="data",
                    className='tab'
                ),
                dmc.Tab(
                    "Execution",
                    icon=DashIconify(icon="carbon:play-outline"),
                    value="execution",
                    className='tab'
                ),
                dmc.Tab(
                    "Judge",
                    icon=DashIconify(icon="streamline:legal-justice-hammer-hammer-work-legal-mallet-office-company-gavel-justice-judge-arbitration-court"),
                    value="judge",
                    className='tab'
                ),
                dmc.Tab(
                    "Help",
                    icon=DashIconify(icon="material-symbols:help"),
                    value="help",
                    className='tab'
                ),
            ]
        ),
        dmc.TabsPanel(tab1_content, value="performance"),
        dmc.TabsPanel(tab2_content, value="data"),
        dmc.TabsPanel(tab3_content, value="execution"),
        dmc.TabsPanel(tab4_content, value="judge"),
        dmc.TabsPanel(help_content, value="help"),
    ],
    value="performance",
    className='tabs-contena',
)

layout = dmc.NotificationsProvider(
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(sidebar, id='side' ,width=3, className='bg-light', style={}),
                dbc.Col(
                    dbc.Row([
                        html.A(
                            DashIconify(
                                icon="ion:logo-github", 
                                width=40,
                                className='icon' 
                            ),
                            href='https://github.com/nozomuorita/visualization-web-app',
                            target='_blank'
                        ),
                        tabs
                    ], id='top'),
                    width=9,
                    id='content',
                    style={},
                    className=''
                ),
                dbc.Row(footer, style={}, className='')
            ]
        ),
    ],fluid=True
    )
)