# modules.etc --------------------------------------------------------------------------------------------------------
import os
import sys
import pandas as pd
import numpy as np
import time
import re
# import pyper
import pickle
from datetime import datetime
from datetime import timedelta
# from selenium.webdriver import Chrome, ChromeOptions
# import requests
# from bs4 import BeautifulSoup

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
# import dash_bootstrap_components as dbc
from dash import html
import dash_bootstrap_components as dbc
# from dash import dcc
# import plotly.figure_factory as ff
# from dash.dependencies import Input, Output, State

# Data, Settings-----------------------------------------------------------------------------------------------------------

# df：業種別株価データ(2001/04/01-2022/03/31)，欠損値なし
# インデックスは日付
df = pd.read_csv(r'../data/origin/stock_2001-2022.csv', index_col='Date', parse_dates=True)

# 業種越株価リターンデータ(2001/06/28~2022/03/31)
# インデックスは日付
# リターン計算期間：3ヶ月
df_r = pd.read_csv("../data/origin/df_r.csv", index_col=0, parse_dates=True)

# df_mergeに上昇ラベルをつけたデータ(2001/06/28~2021/12/29)
# インデックスは日付，TOPIXデータ有
# リターン計算期間：3ヶ月
# 局面閾値：5％
df_label = pd.read_csv("../data/origin/df_label.csv", index_col=0, parse_dates=True)
df_label_train = pd.read_csv("../data/origin/df_label_train.csv", index_col=0, parse_dates=True) # 10年
df_label_test = pd.read_csv("../data/origin/df_label_test.csv", index_col=0, parse_dates=True) # 11年

industries = ['TOPIX', '空運業', '銀行業', '化学', '建設業', '情報・通信業', '電気機器', '電気・ガス業', 'その他金融業', '水産・農林業', '食料品',\
            'ガラス・土石製品', '保険業', '機械', '金属製品', '鉱業', 'その他製品', '非鉄金属', 'パルプ・紙', '石油・石炭製品', '医薬品', '精密機器',\
            '陸運業', '小売業', '不動産業', 'ゴム製品', '証券・商品先物取引業', '海運業', '鉄鋼', 'サービス業', '輸送用機器', '繊維製品', '卸売業',\
            '倉庫・運輸関連業', 'Market', 'Size', 'Value']

pd.set_option("display.max_columns", 200)
pd.set_option("display.max_rows", 200)
pd.set_option("display.max_colwidth", 150)

colors_Plotly = px.colors.qualitative.Plotly
colors_D3 = px.colors.qualitative.D3
colors_G10 = px.colors.qualitative.G10
colors_Dark24 = px.colors.qualitative.Dark24
colors_Light24 = px.colors.qualitative.Light24
colors_Phase = px.colors.cyclical.Phase
colors_mygbm = px.colors.cyclical.mygbm
color_Bold = px.colors.qualitative.Bold

color_palettes = [colors_Plotly, colors_D3, colors_G10, colors_Dark24, colors_Light24, colors_Phase, colors_mygbm, color_Bold]

# function---------------------------------------------------------------------------------------------------------------
def plot_stock_price(data: pd.DataFrame, index: list, start_date: pd.Timestamp, end_date: pd.Timestamp, graph_type: int, color_palette: int):
    """Plot stock prices for specified dates and stocks

    Args:
        data (pd.DataFrame): Original data
        index (list): Stocks to plot
        start_date (pd.Timestamp): Date to start plot
        end_date (pd.Timestamp): Date to end plot
        graph_type (int): Graph of stock price for 0 and average return for 1
        color_palette (int): The color palette to use for the graph, index number of color_palettes.

    Returns:
        plotly.Figure: Plotted graph
    """
    layout = go.Layout(
        xaxis={
            'title':{
            'text': 'Date',
            'font': {'size': 20}
            },
            'tickfont': {'size': 15},
        },
        yaxis={
            'title':{
                    'text': 'Stock Price' if graph_type==0 else 'Return Avg',
                    'font': {'size': 20}
            },
            'tickfont': {'size': 15},
        },
    )
    fig = go.Figure(layout=layout)
    fig.update_layout(
        margin=dict(l=30, r=30, t=30, b=30),
        modebar_remove=[
            'toImage',  # 画像ダウンロード
            # 'zoom2d',  # ズームモード
            # 'pan2d',  # 移動モード
            'select2d',  # 四角形で選択
            'lasso2d',  # ラッソで選択
            # 'zoomIn2d',  # 拡大
            # 'zoomOut2d',  # 縮小
            'autoScale2d',  # 自動範囲設定
            'resetScale2d',  # 元の縮尺
        ],
        font_size=15, 
        hoverlabel_font_size=15
    )
    
    x = []
    for i in data.index:
        if start_date <= i <= end_date:
            x.append(i)
    
    color_palette = color_palettes[color_palette]
    for i in range(len(index)):
        idx = index[i]
        y = list(data.loc[x, idx])
        trace = go.Scatter(x=x, y=y, name=idx, showlegend=True, line={'color': color_palette[i%len(color_palette)]})
        fig.add_trace(trace)
        
    return fig


def sharpe_chart(seed_num: int, use_num: int, entry_num: int, train_test: int):
    """
    Plotting a Sharpe Ratio Chart

    Args:
        seed_num (int): Data number
        use_num (int): Number of rules used to determine the game
        entry_num (int): How many rules to enter if they fit
        train_test (int): Learning data or test data (0: train, 1: test)
        
    Returns:
        plotly.Figure: Graph plotting the Sharpe ratio
    """
    train_test = 'test' if train_test else 'test'
    data = pd.read_csv(f'../data/sharpe_df/{train_test}/sharpe_df{seed_num}.csv', index_col=0)
    layout = go.Layout(
        xaxis={
            'title':{
            'text': 'Risk',
            'font': {'size': 15}
        },
        },
        yaxis={
            'title':{
                    'text': 'Return(Avg.)',
                    'font': {'size': 15}
            },
        },
    )
    
    fig = go.Figure(layout=layout)
    fig.update_layout(
        margin=dict(l=10, r=20, t=10, b=10),
        paper_bgcolor='rgb(236,240,241)',
        plot_bgcolor='rgb(236,240,241)', 
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        modebar_remove=[
            'toImage',  # 画像ダウンロード
            'zoom2d',  # ズームモード
            'pan2d',  # 移動モード
            'select2d',  # 四角形で選択
            'lasso2d',  # ラッソで選択
            'zoomIn2d',  # 拡大
            'zoomOut2d',  # 縮小
            'autoScale2d',  # 自動範囲設定
            'resetScale2d',  # 元の縮尺
        ],
        font_size=8, 
        hoverlabel_font_size=12
    )
    fig.update_xaxes(tickfont_size=9, title_font_size=12)
    fig.update_yaxes(tickfont_size=9, title_font_size=12)
    ##97c5e8 #2b7bba
    n = int(max(data['リスク'].to_list()) * 1000 + 3)
    sharpe_ratio1 = go.Scatter(x=[i*0.001 for i in range(0, n, 1)], y=[i*0.001 for i in range(0, n, 1)], name='Sharpe ratio 1', \
                            line={'color': '#007c89'}, showlegend=False)
    sharpe_ratio2 = go.Scatter(x=[i*0.001 for i in range(0, n, 1)], y=[2*i*0.001 for i in range(0, n, 1)], name='Sharpe ratio 2', \
                            line={'color': '#007c89'}, showlegend=False)
    trace1 = go.Scatter(x=data['リスク'].to_list(), y=data['期待リターン'].to_list(), mode='markers', name='data',
                        marker={'color': '#5a70b1'}, showlegend=False)
    x_highlight = [data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]['リスク'][0]]
    y_highlight = [data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]['期待リターン'][0]]
    trace2 = go.Scatter(x=x_highlight, y=y_highlight, mode='markers', name='selected data',
                        marker={'color': 'rgb(255, 0, 0)'}, showlegend=False)
    
    fig.add_traces([trace1, trace2, sharpe_ratio1, sharpe_ratio2])
    
    return fig

def sharpe_data_txt(seed_num: int, use_num: int, entry_num: int, train_test: int):
    """
    Obtain risk and return under specified conditions

    Args:
        seed_num (int): Data number
        use_num (int): Number of rules used to determine the game
        entry_num (int): How many rules to enter if they fit
        train_test (int): Learning data or test data (0: train, 1: test)
        
    Returns:
        float, float: Risk, Expected Returns
    """
    train_test = 'test' if train_test else 'train'
    data = pd.read_csv(f'../data/sharpe_df/{train_test}/sharpe_df{seed_num}.csv', index_col=0)
    risk = data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]['リスク'].to_list()[0]
    rtn_avg = data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]['期待リターン'].to_list()[0]
    risk = round(risk, 3)
    rtn_avg = round(rtn_avg, 3)

    return risk, rtn_avg


def trade_chart(seed_num: int, use_num: int, entry_num: int, train_test: int):
    """
    Plot a graph of the transactions.

    Args:
        seed_num (int): Data number
        use_num (int): Number of rules used to determine the game
        entry_num (int): How many rules to enter if they fit
        train_test (int): Learning data or test data (0: train, 1: test)
        
    Returns:
        plotly.Figure: Graphs plotting transactions
    """
    
    train_test = 'test' if train_test else 'train'
    data = pd.read_csv(f'../data/ruiwa_df/{train_test}/ruiwa_df{seed_num}.csv', index_col=0)
    
    layout = go.Layout(
        xaxis={
            'title':{
            'text': 'Risk',
            'font': {'size': 15}
        },
        },
        yaxis={
            'title':{
                    'text': 'Return(Avg.)',
                    'font': {'size': 15}
            },
        },
    )
    fig = make_subplots(specs=[[{'secondary_y': True}]])
    fig.update_layout(
        margin=dict(l=30, r=10, t=10, b=10),
        paper_bgcolor='rgb(236,240,241)',
        plot_bgcolor='rgb(236,240,241)',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        modebar_remove=[
            'toImage',  # 画像ダウンロード
            'zoom2d',  # ズームモード
            'pan2d',  # 移動モード
            'select2d',  # 四角形で選択
            'lasso2d',  # ラッソで選択
            'zoomIn2d',  # 拡大
            'zoomOut2d',  # 縮小
            'autoScale2d',  # 自動範囲設定
            'resetScale2d',  # 元の縮尺
        ],
        font_size=8, 
        hoverlabel_font_size=12
    )
    fig.update_xaxes(tickfont_size=9, title_font_size=12)
    fig.update_yaxes(tickfont_size=10, title_font_size=12)
    fig.update_yaxes(tickfont_size=10, title_font_size=12, secondary_y=True)
    
    h1 = data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]['エントリー日'].to_list()
    h2 = data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]['決済日'].to_list()
    r_list = data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]['各リターン'].to_list()
    sum_list = data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]['累和リターン'].to_list()
                
    h3 = h1.copy() # 累和リターンをプロットする日付(累和リターンが変化する日付)
    h3.extend(h2)
    h3.sort()
    if train_test=='test':
        h3.insert(0, df_label_test.index[0])
        h3.append(df.index[-1])
    else:
        h3.insert(0, df.index[0])
        h3.append(df_label_train.index[-1])
    sum_list2 = [] # 累和リターンの値
    for i in range(len(sum_list)):
        sum_list2.append(sum_list[i])
        sum_list2.append(sum_list[i])    
    sum_list2.insert(0, 0)
    sum_list2.insert(0, 0)

    trace1 = go.Scatter(x=h3, y=sum_list2, name='累和リターン', showlegend=False, line={'color': '#8c1d47'})
    
    # Trading period
    shapes = []
    for i in range(len(h1)):
        if r_list[i] > 0.05:
            #color = 'rgb(239, 85, 59)'
            color = '#eb0b03'
            opacity = 0.5
        elif r_list[i]>0:
            color = 'rgb(0, 204, 150)'
            color = '#3ec443'
            opacity = 0.5
        else:
            color = 'rgb(99, 110, 250)'
            color = '#3b95d3'
            opacity = 0.5
            
        s = go.layout.Shape(
                type='rect',
                xref='x',
                yref='paper',
                x0=h1[i],
                x1=h2[i],
                y0=0,
                y1=1,
                #fillcolor='LightSalmon',
                fillcolor=color,
                opacity=opacity,
                layer='below',
                line={'width': 0}
            )
        shapes.append(s)

    # topix trace
    if train_test=='train':
        start, end = '2001-04-02', '2011-03-31'
    else:
        start, end = '2011-04-01', '2022-03-31'
    trace2 = go.Scatter(x=df.index[df.index.get_loc(start):df.index.get_loc(end)+1],
                        y=df.iloc[df.index.get_loc(start):df.index.get_loc(end)+1, 0], 
                        name='TOPIX',
                        showlegend=False,
                        line={'color': '#5c619f'})
    
    fig.add_trace(trace1, secondary_y=True)
    fig.add_trace(trace2)
    fig.update_layout(shapes=shapes)
    if train_test=='test':
        fig.update_xaxes(tickvals=[int(_) for _ in range(2011, 2023)])
    else:
        fig.update_xaxes(tickvals=[int(_) for _ in range(2001, 2013)])

    fig.update_yaxes(title={'text': 'Stock Price'}, showgrid=False,)
    fig.update_yaxes(secondary_y=True, title={'text': 'Cumulative Return'}, showgrid=False)

    return fig

def trade_data_txt(seed_num: int, use_num: int, entry_num: int, train_test: int):
    """
    Obtain cumulative returns and number of transactions under specified conditions

    Args:
        seed_num (int): Data number
        use_num (int): Number of rules used to determine the game
        entry_num (int): How many rules to enter if they fit
        train_test (int): Learning data or test data (0: train, 1: test)
        
    Returns:
        float, int: Cumulative return, number of transactions
    """
    train_test = 'test' if train_test else 'train'
    data = pd.read_csv(f'../data/ruiwa_df/{train_test}/ruiwa_df{seed_num}.csv', index_col=0)

    if len(data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]['累和リターン'].to_list())==0:
        cum_return = 0
        trade_num = 0
    else:
        trade_data = data[(data['使用ルール数']==use_num) & (data['エントリールール数']==entry_num)]\
            ['累和リターン'].to_list()
        #print(trade_data)
        cum_return=round(trade_data[-1], 3)
        trade_num = len(trade_data)
            
    return cum_return, trade_num

def rule_table_chart(seed_num: int, use_num: int, train_test: int):
    """
    Create a table graph of the rules used

    Args:
        seed_num (int): Data number
        use_num (int): Number of rules used to determine the game
        train_test (int): Learning data or test data (0: train, 1: test)
        
    Returns:
        plotly.Figure: Table Graph of Rules
    """

    train_test = 'test' if train_test else 'train'
    data = pd.read_csv(f"../data/cd_sorted/{train_test}/cd_sorted{seed_num}.csv", index_col=0)
    data_sorted = data[data['freq']>0.05]
    
    rows = []
    for i in range(use_num):
        d = 0
        row = html.Tr([html.Td(round(data_sorted.iloc[i, 0], 3)), html.Td(data_sorted.iloc[i, 3])])
        rows.append(row)

    table_header = [
        html.Thead(html.Tr([html.Th(" Lift "), html.Th("Rules")]))
    ]
    table_body = [html.Tbody(rows)]
    table = dbc.Table(table_header + table_body, bordered=True, hover=True, striped=True, id='tab1_table1', className='text-center table-chart')
    
    return table


def industry_freq_chart(seed_num: int, use_num: int):
    """
    Graph the frequency of the industry

    Args:
        seed_num (int): Data number
        use_num (int): Number of rules used to determine the game
        
    Returns:
        plotly.Figure: Graphs plotting frequency
    """
    
    data1 = pd.read_csv(f'../data/cd_sorted/train/cd_sorted{seed_num}.csv', index_col=0)
    data2 = pd.read_csv(f'../data/rd_sorted/rd_sorted{seed_num}.csv', index_col=0)
    
    use_index = data1[data1['freq']>0.05].index[:use_num]
    data = data2.loc[use_index, :]
    
    ind, flag, value = [], [], []
    under, top = [], []
    for i in range(use_num):
        for j in range(len(data.columns)//3):
            if not(pd.isnull(data.iloc[i, 3*j])):
                ind.append(data.iloc[i, 3*j])
            if not(pd.isnull(data.iloc[i, 3*j+1])):
                flag.append(data.iloc[i, 3*j+1])
                value.append(data.iloc[i, 3*j+2])
                if (data.iloc[i, 3*j+1]=='>=') or (data.iloc[i, 3*j+1]=='>'):
                    top.append(1.0)
                    under.append(data.iloc[i, 3*j+2])
                elif (data.iloc[i, 3*j+1]=='<=') or (data.iloc[i, 3*j+1]=='<'):
                    top.append(data.iloc[i, 3*j+2])
                    under.append(-1.0)

    layout = go.Layout(yaxis={'title': {'text': 'Past 3-Month Return'}})
    fig = go.Figure(layout=layout)
    traces = []
    for i in range(len(under)):
        trace = go.Box(y=[under[i], top[i]], name=ind[i], marker={'color': 'rgb(36, 73, 147)'}, opacity=0.3,\
                       line={'width': 0}, showlegend=False)
        traces.append(trace)
        
    fig.add_traces(traces)
    fig.update_layout(
        yaxis=dict(range=(-0.95, 0.95)),
        margin=dict(l=30, r=10, t=10, b=10),
        paper_bgcolor='rgb(236,240,241)',
        plot_bgcolor='rgb(236,240,241)',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        modebar_remove=[
            'toImage',  # 画像ダウンロード
            'zoom2d',  # ズームモード
            'pan2d',  # 移動モード
            'select2d',  # 四角形で選択
            'lasso2d',  # ラッソで選択
            'zoomIn2d',  # 拡大
            'zoomOut2d',  # 縮小
            'autoScale2d',  # 自動範囲設定
            'resetScale2d',  # 元の縮尺
        ],
        font_size=12, 
        hoverlabel_font_size=12
    )
   
    return fig