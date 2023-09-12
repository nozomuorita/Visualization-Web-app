import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

tab4_content = html.Div([
    DashIconify(icon="ic:round-construction", width=100),
    html.H4('Under Construction', className='mt-3 ml-3'),
], className='mb-4 tab3-contena'
)