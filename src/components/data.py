import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from datetime import date

idx_list = ['TOPIX', '空運業', '銀行業', '化学', '建設業', '情報・通信業', '電気機器', '電気・ガス業', 'その他金融業', '水産・農林業', '食料品', 'ガラス・土石製品',\
        '保険業', '機械', '金属製品', '鉱業', 'その他製品', '非鉄金属', 'パルプ・紙', '石油・石炭製品', '医薬品', '精密機器', '陸運業', '小売業', '不動産業',\
        'ゴム製品', '証券・商品先物取引業', '海運業', '鉄鋼', 'サービス業', '輸送用機器', '繊維製品', '卸売業', '倉庫・運輸関連業', 'マーケット', \
        'サイズ', 'バリュー']


# tab2 --------------------------------------------------------------------------------------------------------
# select-box
collapse = html.Div([
    dmc.ActionIcon(
        DashIconify(icon="clarity:settings-line", width=20),
        variant="filled",
        id="setting-btn",
        n_clicks=0,
        mb=10,
        className='mt-1'
    ),
    dbc.Collapse(
        dbc.Card(
            dbc.CardBody(
                html.Div([
                    html.P('Color Palette', className='mb-2 fs-6'),
                    dbc.RadioItems(
                        options=[
                            {"label": "Plotly", "value": 0},
                            {"label": "D3", "value": 1},
                            {"label": "G10", "value": 2},
                            {"label": "Dark24", "value": 3},
                            {"label": "Light24", "value": 4},
                            {"label": "Phase", "value": 5},
                            {"label": "mygbm", "value": 6},
                            {"label": "Bold", "value": 7},
                        ],
                        value=3,
                        id="radioitems-color-palette",
                        inline=True,
                    ),
                ], className='color-palette-collapse'),
                className='collapse-cardbody p-2'
            )
        ),
        id="collapse",
        is_open=False,
        className=''
    ),
], className='')

select_box = html.Div([
    
    html.H5('銘柄', className='text-white fw-bold'),
    # dcc.Dropdown(id='stock-index', multi=True,
    #                 value=0,
    #                 options=[{'label': x, 'value': i}
    #                         for i, x in enumerate(list(app_base.df.columns))],
    #             ),
    dmc.MultiSelect(
        placeholder="Select index",
        id="stock-index",
        value=[0, 1],
        data=[
            {"value": i, "label": x}
            for i, x in enumerate(idx_list[:-3])
        ],
        clearable=True,
        className='selecter-index',
        #style={"width": 400, "marginBottom": 10},
    ),
    
    html.H5('開始日', className='text-white fw-bold'),
    # dcc.DatePickerSingle(
    #     id='start-date',
    #     min_date_allowed=date(2001, 4, 1),
    #     max_date_allowed=date(2023, 8, 31),
    #     initial_visible_month=date(2001, 4, 1),
    #     date=date(2001, 4, 1),
    #     className='calendar'
    # ),
    dmc.DatePicker(
        id='start-date',
        value=date(2001, 4, 1),
        icon=DashIconify(icon="clarity:date-line"),
        inputFormat="YYYY/MM/DD",
        minDate=date(2001, 4, 1),
        maxDate=date(2022, 3, 31),
        className='calendar'
    ),
    
    html.H5('終了日', className='text-white fw-bold'),
    # dcc.DatePickerSingle(
    #     id='end-date',
    #     min_date_allowed=date(2001, 4, 1),
    #     max_date_allowed=date(2023, 8, 31),
    #     initial_visible_month=date(2022, 3, 31),
    #     date=date(2022, 3, 31),
    #     className='calendar'
    # ),
    dmc.DatePicker(
        id='end-date',
        value=date(2022, 3, 31),
        icon=DashIconify(icon="clarity:date-line"),
        inputFormat="YYYY/MM/DD",
        minDate=date(2001, 4, 1),
        maxDate=date(2022, 3, 31),
        className='calendar'
    ),


    dbc.Button("Apply",
                color="#ffffff",
                className="me-1 fw-bolder nav-button bg-secondary",
                id='btn2',
                n_clicks=0
    ),

], className='select-box')

graph_4 = html.Div([
                dbc.Spinner(dcc.Graph(className='tab1-fig', id='tab2-fig1', config={'displaylogo': False}), color='light'),
            ])
graph_contena4 = dbc.Row(
    [
        dbc.Col(graph_4, width=12)
    ], className='mt-3'
)
graph_5 = html.Div([
                dbc.Spinner(dcc.Graph(className='tab1-fig', id='tab2-fig2', config={'displaylogo': False}), color='light'),
            ])
graph_contena5 = dbc.Row(
    [
        dbc.Col(graph_5, width=12)
    ], className='mt-3'
)


tab2_content = html.Div([
    dbc.Card(
        dbc.CardBody(
            [
                html.Div([
                    html.P("Stock Price Data", className="text-white fs-4 fw-bolder m-0 p-0 me-2"),
                    collapse,
                ], className='tab2-title'),
                html.Hr(className='text-white'),
                select_box,
                html.P('Stock Price', className='text-white fs-5 fw-bolder mt-2'),
                graph_contena4,
                html.P('Past 3-Month Return', className='text-white fs-5 fw-bolder mt-3'),
                graph_contena5,
            ]
        ),
        className="mt-3 bg-primary",
    ),
], className='mb-4'
)
