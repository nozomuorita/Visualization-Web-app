# Help Tab
import dash_bootstrap_components as dbc
from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

help = html.Div([
    dbc.Card(
        dbc.CardBody(
            [
                html.P("Help Page", className="text-white fs-4 fw-bolder mb-0"),
                html.Hr(className='text-white mt-0'),
                
                html.H4('Overview', className='text-white fw-bold mt-4 mb-0'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.P('・分析結果の可視化をすることができます。', className='text-white mb-0 fs-6 text-indent'),
                html.P('・サイドバーでパラメータを選択し、Applyボタンをクリックすると、右側にグラフが表示されます。', className='text-white fs-6 text-indent'),
                
                html.H4('Tools', className='text-white fw-bold mt-4 mb-0'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.Span(
                    [
                        dbc.Badge("Python", color="success", className="me-1 mb-2"),
                        dbc.Badge("R", color="success", className="me-1 mb-2"),
                        dbc.Badge("Visual Studio Code", color="secondary", className="me-1 mb-2"),
                        dbc.Badge("plotly dash", color="info", className="me-1 mb-2"),
                    ]
                ),
                
                html.Br(),
                
                html.H4('Usage', className='text-white fw-bold mt-4 mb-0'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.H5('Setting(Sidebar)', className='text-white mb-0'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.Div([
                    html.Img(src='assets/img/setting.png', style={'width': '250px'}, className='my-2'),
                    html.Div([
                       html.P('・学習 or テスト: 学習データかテストデータを選択します。', className='text-white fs-6 text-indent ms-3 my-2'),
                       html.P('・Seed: データ番号を選択します(30回分の結果データがあります)。', className='text-white fs-6 text-indent ms-3 my-2'),
                       html.P('・使用ルール数: 局面の判断に使用するルール数を選択します。', className='text-white fs-6 text-indent ms-3 my-2'),
                       html.P('・エントリールール数: いくつのルールが適合した時にエントリーするか選択します。', className='text-white fs-6 text-indent ms-3 my-2'),
                       html.P('・局面: 上昇局面か下落局面を選択します。', className='text-white fs-6 text-indent ms-3 my-2'),
                       html.P('・Applボタン: クリックすることで選択条件をグラフへ適用します。', className='text-white fs-6 text-indent ms-3 my-2'),
                    ], className='help-subsection'),
                ], className='d-flex help-section mb-2'),
                html.Div([
                    html.Img(src='assets/img/pie-chart.png', style={'width': '250px'}, className='my-2'),
                    html.Div([
                       html.P('・説明変数の割合を表す円グラフです。', className='text-white fs-6 text-indent ms-3 my-2'),
                       html.P('・”学習”にチェックがついているときは学習データ、”テスト”にチェックがついているときはテストデータの割合が表示されます。', className='text-white fs-6 text-indent ms-3 my-2'),
                    ], className='help-subsection'),
                ], className='d-flex help-section mb-2'),
                
                html.Br(),
                
                html.H5('Performance(Tab1)', className='text-white mb-0'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.Div([
                    html.Div([
                        html.Img(src='assets/img/tab1-1.png', style={'width': '500px'}, className='my-2'),
                        html.Img(src='assets/img/tab1-2.png', style={'width': '500px'}, className='my-2'),
                    ], className='', style={'width': '500px'}),
                    html.Div([
                        dmc.Alert(
                            "Download png button is not available(under construction).",
                            title="Note",
                            color='green',
                            icon=DashIconify(icon='mingcute:warning-line'),
                            className='ms-2 mb-2'
                        ),
                        html.P('・左上：シャープレシオグラフ。選択したSeedのすべてのデータが表示され、選択した条件のデータは赤い点で表示されます。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('・グラフ下に、選択した条件でのリスクと期待リターンが表示されます。', className='text-white fs-6 text-indent ms-2 my-2'),
                        html.P('・右上：選択した条件が局面と判断した期間とその取引のリターンが表示されます。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('・背景色の部分で取引が行われています(赤：リターン5%以上、緑：リターン0~5%、青：リターン0%未満)', className='text-white fs-6 text-indent ms-2 my-2'),
                        html.P('・グラフ下に、選択した条件での累和リターンと取引回数が表示されます。', className='text-white fs-6 text-indent ms-2 my-2'),
                        html.P('・中央：使用した判別ルールの一覧とそのLift値が表示されます。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('・下：選択した条件に出現する業種を濃度で表示します。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('【グラフに関して】', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('・見たい範囲をドラッグして選択することで拡大表示ができます。', className='text-white fs-6 text-indent ms-2 my-2'),
                        html.P('・ダブルクリックをすることで元の表示に戻ります。', className='text-white fs-6 text-indent ms-2 my-2'),
                    ], className='help-subsection m-0 p-0'),
                ], className='d-flex help-section mb-2'),
                
                html.Br(),
                
                html.H5('Data(Tab2)', className='text-white mb-0'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.Div([
                    html.Div([
                        html.Img(src='assets/img/tab2-1.png', style={'width': '500px'}, className='my-2'),
                        html.Img(src='assets/img/tab2-2.png', style={'width': '500px'}, className='my-2'),
                    ], style={'width': '500px'}),
                    html.Div([
                        html.P('・カラーパレット：歯車アイコンをクリックするとグラフのカラーパレットを選択できます。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('・カラーパレットを変更し適用すると、グラフに変更情報が反映されます。', className='text-white fs-6 text-indent ms-2 my-2'),
                        html.P('・銘柄：グラフに表示したい銘柄を選択できます。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('・開始日、終了日：グラフに表示したい範囲を指定できます。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('・Applyボタン：クリックすると変更情報がグラフに反映されます。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('・グラフ(上)：株価データが表示されます。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                        html.P('・グラフ(下)：過去３か月リターンデータが表示されます。', className='text-white fs-6 text-indent ms-2 my-2 mt-4'),
                    ], className='help-subsection'),
                ], className='d-flex help-section mb-2'),
                
                html.Br(),
                
                html.H5('Execution(Tab3)', className='text-white mb-0'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.Div([
                    html.Div([
                        html.Img(src='assets/img/tab3.png', style={'width': '500px'}, className='my-2'),
                    ]),
                    html.Div([
                       html.P('・現在、作成中です。', className='text-white fs-6 text-indent ms-3 my-2'),
                    ], className='help-subsection'),
                ], className='d-flex help-section mb-2'),
                
                html.Br(),
                
                html.H5('Judge(Tab4)', className='text-white mb-0'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.Div([
                    html.Div([
                        html.Img(src='assets/img/tab4.png', style={'width': '500px'}, className='my-2'),
                    ]),
                    html.Div([
                       html.P('・現在、作成中です。', className='text-white fs-6 text-indent ms-3 my-2'),
                    ], className='help-subsection'),
                ], className='d-flex help-section mb-2'),
                
                html.Br(),

                html.H4('Contact', className='text-white fw-bold text-decoration-underline'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.P('E-mail: 23nmxxxx@xx.xxxx.ac.jp', className='text-white'),
                
                html.Br(),
                
                html.H4('References', className='text-white fw-bold text-decoration-underline'),
                html.Hr(className='m-0 p-0 text-white mb-2'),
                html.Div([
                html.A('Github', href='https://github.com/nozomuorita/visualization-web-app', className='text-white', target='_blank'),]),
                # html.Div([
                # html.A('研究概要', href='#', className='text-white', target='_blank'),
                # ], className='mt-2'),
                
                html.Br(),
                
            ]
        ),
        className="mt-3 bg-primary",
    ),
], className='mb-4'
)
