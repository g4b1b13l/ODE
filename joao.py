import pandas as pd
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import cufflinks as cf
init_notebook_mode(connected=True)
cf.go_offline()

import dash
import dash_core_components as dcc
import dash_html_components as html
from navbar import Navbar


nav = Navbar()

#df_2017 = pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\Atividade JOao\\Atividade4\\df_2017.csv',index_col=0)
#df_2018 = pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\Atividade JOao\\Atividade4\\df_2018.csv',index_col=0)

df_2017 = pd.read_csv('Apoio/df_2017.csv',index_col=0)
df_2018 = pd.read_csv('Apoio/df_2018.csv',index_col=0)


fig1 = make_subplots(rows=1, cols=1,row_titles = ['Quantidade de Projetos'],  shared_yaxes=True)

fig1.add_trace(go.Bar(x=df_2017.columns.to_list(), y=df_2017.loc['QUANTIDADE'], name='2017'),1,1)
fig1.update_layout(coloraxis=dict(colorscale='bluered'), showlegend=False)
fig1.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))
fig1.update_layout(title_text='Projetos de Extensão Divididos por Centro', title_x=0.5)

fig1.add_trace(go.Bar(x=df_2018.columns.to_list(), y=df_2018.loc['QUANTIDADE'], name='2018'),1,1)
fig1.update_layout(coloraxis=dict(colorscale='bluered'), showlegend=True)
fig1.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))

fig1.update_layout(
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0)'
)

fig2 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]], subplot_titles=['2017', '2018'])
fig2.update_layout(
    autosize=False,
    width=1300,
    height=500,
    #paper_bgcolor='rgba(0,0,0,0)',
    #plot_bgcolor='rgba(0,0,0,0)'
)

fig2.update_traces(textposition='inside')
#fig2.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig2.add_trace(go.Pie(labels=df_2017.columns.to_list(), values=df_2017.loc['QUANTIDADE'], scalegroup='one', textinfo='label+percent', name='2017'),1, 1)
fig2.add_trace(go.Pie(labels=df_2018.columns.to_list(), values=df_2018.loc['QUANTIDADE'], scalegroup='one', textinfo='label+percent', name='2018'),1, 2)
fig2.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))
fig2.update_layout(title_text='Projetos de Extensão Divididos por Centro em Porcentagem', title_x=0.5)


def joao():
    layout = html.Div([
    nav,
    html.H1('Escolha abaixo qual é a figura que você quer exibir : ',style={'textAlign': 'center', 'margin-top': '15px','margin-bottom': '15px'}),
    dcc.Dropdown(
        id='page-1-dropdown',
        options=[{'label': i, 'value': i} for i in ['Figura1', 'Figura2']], #cria um dropdown (caixa de seleção) com os elementos passados na lista
        value='LA',
        searchable=False
    ),
    html.Div(id='page-1-content',style={'display': 'inline-block','width': '100%'}),
    html.Br(),
    html.Br(),
    html.P([html.Br()],'linebreak?'), #Pula uma linha 
    ])
    return layout

