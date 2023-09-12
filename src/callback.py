from dash.dependencies import Input, Output, State
from func import *
from app import app

@app.callback(Output('pie-chart', 'figure'),
              Input('radioitems-train-test', 'value'))
def update_pie_chart(radio_value):
    if radio_value==1:
        # label_data = app_base.df_label_train['label'].value_counts() / len(app_base.df_label_test)
        label_data = df_label_train['label'].value_counts() / len(df_label_test)
    else:
        # label_data = app_base.df_label_test['label'].value_counts() / len(app_base.df_label_test)
        label_data = df_label_test['label'].value_counts() / len(df_label_test)
        
    df_pie = pd.DataFrame()
    df_pie['name'] = ['up', 'other']
    df_pie['percentage'] = [label_data[0], label_data[1]]
    fig_pie = px.pie(df_pie,
                    values='percentage',
                    names='name',
                    color='name',
                    color_discrete_map={'up':'rgb(36, 73, 147)','other':'rgb(175, 49, 35)',})
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    fig_pie.update_layout(
        margin=dict(l=10, r=10, t=0, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        modebar_remove=[
        'toImage',  # 画像ダウンロード
        ],
        showlegend=False,
    )

    return fig_pie

# entry-num-dropdown
@app.callback(Output('entry-num', 'options'),
              Output('entry-num', 'value'),
              Input('use-num', 'value'),
              )
def update_entry_dropdown(value):
    return [{'label': x, 'value': x} for x in range(1, int(value)+1)], 1

# tab1-callback
# fig1
@app.callback(Output('tab1-fig1', 'figure'),
              Output('tab1-fig1-sub', 'figure'),
              Output('risk', 'children'),
              Output('rtn-avg', 'children'),
              Input('apply-btn', 'n_clicks'),
              State('seed-num', 'value'),
              State('use-num', 'value'),
              State('entry-num', 'value'),
              State('phase', 'value'),
              State('radioitems-train-test', 'value'),
              )
def update_sharpe(n_clicks, seed_num, use_num, entry_num, phase, train_test):
    time.sleep(0.5)
    seed_num = int(seed_num)
    use_num = int(use_num)
    entry_num = int(entry_num)
    phase = int(phase)
    train_test = int(train_test)
        
    # fig = app_base.sharpe_chart(seed_num, use_num, entry_num, train_test)
    # risk, rtn_avg = app_base.sharpe_data_txt(seed_num, use_num, entry_num, train_test)
    fig = sharpe_chart(seed_num, use_num, entry_num, train_test)
    risk, rtn_avg = sharpe_data_txt(seed_num, use_num, entry_num, train_test)
    
    risk_txt = 'Risk: ' + ' ' + str(risk)
    rtn_avg = 'Return(Avg.): ' + ' ' + str(rtn_avg)
    
    return fig, fig, risk_txt, rtn_avg

# fig1 download
# @app.callback(Output('note-success-fig1', 'children'),
#               Input('download-fig1', 'n_clicks'),
#               State('seed-num', 'value'),
#               State('use-num', 'value'),
#               State('entry-num', 'value'),
#               State('phase', 'value'),
#               State('radioitems-train-test', 'value'),
#               )
# def update_trade_char(n_clicks, seed_num, use_num, entry_num, phase, train_test):
#     seed_num = int(seed_num)
#     use_num = int(use_num)
#     entry_num = int(entry_num)
#     phase = int(phase)
#     train_test = int(train_test)

#     if n_clicks > 0:
#         fig = app_base.sharpe_chart(seed_num, use_num, entry_num, train_test)
#         print('made')
#         fig.write_image('figure.png')
#         print('downloaded')
#         return dmc.Notification(
#             title="Download Success!",
#             id="simple-notify",
#             action="show",
#             message="Saved as 'figure1'",
#             color='green',
#             icon=DashIconify(icon="akar-icons:circle-check"),
#         )
 
# fig2   
@app.callback(Output('tab1-fig2', 'figure'),
              Output('tab1-fig2-sub', 'figure'),
              Output('cum_rtn', 'children'),
              Output('transaction', 'children'),
              Input('apply-btn', 'n_clicks'),
              State('seed-num', 'value'),
              State('use-num', 'value'),
              State('entry-num', 'value'),
              State('phase', 'value'),
              State('radioitems-train-test', 'value'),
              )
def update_trade_chart(n_clicks, seed_num, use_num, entry_num, phase, train_test):
    time.sleep(0.5)
    seed_num = int(seed_num)
    use_num = int(use_num)
    entry_num = int(entry_num)
    phase = int(phase)
    train_test = int(train_test)
        
    # fig = app_base.trade_chart(seed_num, use_num, entry_num, train_test)
    # cum_rtn, trade_num = app_base.trade_data_txt(seed_num, use_num, entry_num, train_test)
    fig = trade_chart(seed_num, use_num, entry_num, train_test)
    cum_rtn, trade_num = trade_data_txt(seed_num, use_num, entry_num, train_test)
    cum_rtn_txt = 'Cumulative Return: ' + ' ' + str(cum_rtn)
    trade_num_txt = 'Number of Transactions: ' + ' ' + str(trade_num)
    
    return fig, fig, cum_rtn_txt, trade_num_txt

@app.callback(Output('table-chart', 'children'),
              Input('apply-btn', 'n_clicks'),
              State('seed-num', 'value'),
              State('use-num', 'value'),
              State('phase', 'value'),
              State('radioitems-train-test', 'value'),
              )
def update_table_chart(n_clicks, seed_num, use_num,  phase, train_test):
    time.sleep(0.5)
    seed_num = int(seed_num)
    use_num = int(use_num)
    phase = int(phase)
    train_test = int(train_test)
    
    # fig = app_base.rule_table_chart(seed_num, use_num, train_test)
    fig = rule_table_chart(seed_num, use_num, train_test)
    
    return fig

@app.callback(Output('tab1-fig3', 'figure'),
              Input('apply-btn', 'n_clicks'),
              State('seed-num', 'value'),
              State('use-num', 'value'),
              State('phase', 'value'),
              )
def update_table_chart(n_clicks, seed_num, use_num,  phase):
    time.sleep(0.5)
    seed_num = int(seed_num)
    use_num = int(use_num)
    phase = int(phase)
    
    # fig = app_base.industry_freq_chart(seed_num, use_num)
    fig = industry_freq_chart(seed_num, use_num)
    
    return fig


# tab2-callback
@app.callback(Output('tab2-fig1', 'figure'),
              Output('tab2-fig2', 'figure'),
              Input('btn2', 'n_clicks'),
              State('stock-index', 'value'),
              State('start-date', 'value'),
              State('end-date', 'value'),
              State('radioitems-color-palette', 'value')
            #   Input('stock-index', 'value'),
            #   Input('start-date', 'value'),
            #   Input('end-date', 'value'),
              )
def update_stock_chart(n_clicks, index, start_date, end_date, color_palette):
    time.sleep(0.5)
    start = start_date.split('-')
    start_date = pd.Timestamp(int(start[0]), int(start[1]), int(start[2]))
    end = end_date.split('-')
    end_date = pd.Timestamp(int(end[0]), int(end[1]), int(end[2]))
    
    # columns = list(app_base.df.columns)
    columns = list(df.columns)
    index = [columns[i] for i in index]

    # fig1 = app_base.plot_stock_price(app_base.df, index, start_date, end_date, 0, color_palette)
    # fig2 = app_base.plot_stock_price(app_base.df_r, index, start_date, end_date, 1, color_palette)
    fig1 = plot_stock_price(df, index, start_date, end_date, 0, color_palette)
    fig2 = plot_stock_price(df_r, index, start_date, end_date, 1, color_palette)
    return fig1, fig2

@app.callback(
    Output("collapse", "is_open"),
    Input("setting-btn", "n_clicks"),
    State("collapse", "is_open"),
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
