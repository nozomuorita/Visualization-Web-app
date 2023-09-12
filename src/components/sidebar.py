import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

sidebar = html.Div(
    [
        # setting-header
        dbc.Row(
            [
                html.Div([
                    html.A(html.H5('Settings'), href='#top'),
                    html.Img(src="assets/img/dash-new-logo.webp", className='dash-icon'),
                ], className='setting-header-content',
                ),
            ],
            className='text-white bg-primary setting-header'
            ),
        
        # Condition selection part
        dbc.Row(
            [
                html.Div([    
                    dbc.RadioItems(
                        options=[
                            {"label": "学習", "value": 0,},
                            {"label": "テスト", "value": 1},
                        ],
                        value=0,
                        id="radioitems-train-test",
                        inline=True,
                        className='fw-bolder train-test'
                    ),

                    html.P('Seed', className='fw-bolder'),
                    dbc.Select(
                        id="seed-num",
                        value=1,
                        options=[{"label": x, "value": x} for x in range(1, 30+1)],
                    ),
                    
                    html.P('使用ルール数', className='fw-bolder'),
                    dbc.Select(
                        id="use-num",
                        value=1,
                        options=[{"label": x, "value": x} for x in range(1, 20+1)],
                    ),
                    
                    html.P('エントリールール数', className='fw-bolder'),
                    dbc.Select(
                        id="entry-num",
                        value=1,
                        options=[{"label": x, "value": x} for x in range(1, 20+1)],
                    ),
                    
                    html.P('局面', className='fw-bolder'),
                    dbc.Select(
                        id="phase",
                        value=1,
                        options=[{"label": '上昇', "value": 1},
                                 {"label": "下落(disabled)", "value": 0, "disabled": True}],
                    ),

                    html.Div([
                        # dbc.Button("Apply",
                        #            color="#ffffff",
                        #            className="me-1 fw-bolder nav-button",
                        #            id='my-button',
                        #            n_clicks=0
                        # ),  
                        dmc.Button(
                            "Apply",
                            className='me-1 fw-bolder nav-button',
                            id='apply-btn',
                            n_clicks=0,
                            color='#ffffff',
                            rightIcon=DashIconify(icon="material-symbols:search"),
                            radius=25,
                            size='sm'
                        ),      
                    ], className='button-contena'
                    ),
                    
                    html.Hr(),
                ], className='setting-content'
                )
            ], className='select-part'
            #style={'height': '55vh', }
        ),

        # Objective Variable Percentage Graph
        dbc.Row(
            [
                html.Div([
                    html.P('Target Variables', className='fw-bolder'),
                    dcc.Graph(id='pie-chart', config={'displaylogo': False})
                ])
            ], className='target-variable'
        ),
    ], className='setting'
)