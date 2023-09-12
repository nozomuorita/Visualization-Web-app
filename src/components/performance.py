import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# tab1 --------------------------------------------------------------------------------------------------------------
# card1
card_1_1 = dbc.Spinner(dbc.Card(
            dbc.CardBody(
                [
                    html.Div([
                        html.Div([
                            html.H5(id='risk', className=''),
                            html.H5(id='rtn-avg', className=''),
                        ]),
                    html.Div(
                        [
                            html.Div(id="note-success-fig1"),
                            dmc.Button(
                                "Download png",
                                className='me-1 fw-bolder nav-button bg-success mt-3',
                                n_clicks=0,
                                variant='filled',
                                color='success',
                                rightIcon=DashIconify(icon="zondicons:download"),
                                radius=5,
                                size='sm',
                                id='download-fig1'
                            ),
                        ]
                    )
                    ], className='card-contena'),   
                ]
            )
           ), color='primary')
card_1_2 = dbc.Spinner(dbc.Card(
            dbc.CardBody(
                [
                    html.Div([
                        html.Div([
                            html.H5(id='cum_rtn'),
                            html.H5(id='transaction'),
                        ]),
                        dmc.Button(
                            "Download png",
                            className='me-1 fw-bolder nav-button bg-success mt-3',
                            #id='mt-button',
                            n_clicks=0,
                            variant='filled',
                            color='success',
                            rightIcon=DashIconify(icon="zondicons:download"),
                            radius=5,
                            size='sm'
                        ),
                    ], className='card-contena'),   
                ]
            )
           ), color='primary')
card_contena1 = dbc.Row(
    [
        dbc.Col(card_1_1, width=5),
        dbc.Col(card_1_2, width=7),
    ], className='mt-3'
)

graph_1_1 = dbc.Spinner(dcc.Graph(className='tab1-fig', id='tab1-fig1', config={'displaylogo': False}), color='light')
graph_1_2 = dbc.Spinner(dcc.Graph(className='tab1-fig', id='tab1-fig2', config={'displaylogo': False}), color='light')
graph_1_1_sub = dbc.Spinner(dcc.Graph(className='tab1-fig', id='tab1-fig1-sub', config={'displaylogo': False}), color='light')
graph_1_2_sub = dbc.Spinner(dcc.Graph(className='tab1-fig', id='tab1-fig2-sub', config={'displaylogo': False}), color='light')
graph_contena1 = dbc.Row(
    [
        dbc.Col(graph_1_1, width=5),
        dbc.Col(graph_1_2, width=7),
    ], className='mt-3 graph-contena1'
)

# max-width: 1200px
graph_contena1_sub = dbc.Row(
    [
        dbc.Row([
            dbc.Col(
                graph_1_1_sub, width=12
            ) 
        ], className='mb-3'),
        dbc.Row([
            dbc.Col(
                graph_1_2_sub, width=12
            )
        ])
    ], className='mt-3 graph-contena1-sub'
)

# card2
graph_2_1 = html.Div([
                dbc.Spinner(color='primary', id='table-chart'),
            ]
            )
graph_contena2 = dbc.Row(
    [
        dbc.Col(graph_2_1, width=12)
    ], className='mt-3'
)

# card3
graph_3_1 = html.Div([
                dbc.Spinner(dcc.Graph(className='tab1-fig', id='tab1-fig3', config={'displaylogo': False}), color='light'),
            ])
graph_contena3 = dbc.Row(
    [
        dbc.Col(graph_3_1, width=12)
    ], className='mt-3'
)

tab1_content = html.Div([
    dbc.Card(
        dbc.CardBody(
            [
                html.P("シャープレシオ・取引の様子", className="card-text text-white fs-4 fw-bolder"),
                graph_contena1,
                graph_contena1_sub,
                card_contena1
            ]
        ),
        className="mt-3 bg-primary",
    ),
    dbc.Card(
        dbc.CardBody(
            [
                html.P("判別ルールリスト", className="text-black fs-4 fw-bolder"),
                graph_contena2
            ],
        ),
        className="mt-3 bg-light",
    ),
    dbc.Card(
        dbc.CardBody(
            [
                html.P("業種頻出度", className="text-white fs-4 fw-bolder"),
                graph_contena3
            ],
        ),
        className="mt-3 bg-primary",
    ),
], className='mb-3'
)