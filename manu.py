import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
import plotly.graph_objs as go
import plotly.offline as py
plotly.offline.init_notebook_mode(connected =True)






from navbar import Navbar


nav = Navbar()

#dataset_2017 = pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\atividade4_manu\\dataset_2017.csv')
#dataset_2018 = pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\atividade4_manu\\dataset_2018.csv')
#dataset_2019 = pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\atividade4_manu\\dataset_2019.csv')

dataset_2017 = pd.read_csv('Apoio\\dataset_2017.csv')
dataset_2018 = pd.read_csv('Apoio\\dataset_2018.csv')
dataset_2019 = pd.read_csv('Apoio\\dataset_2019.csv')

dataset_2017.index= ['Total']
dataset_2018.index= ['Total']
dataset_2019.index= ['Total']
dataset_2017.drop('Unnamed: 0',axis  = 1,inplace = True)
dataset_2018.drop('Unnamed: 0',axis  = 1,inplace = True)
dataset_2019.drop('Unnamed: 0',axis  = 1,inplace = True)


data2 = [ go.Bar(x=dataset_2018.loc['Total'].index,
               y=dataset_2018.loc['Total'].values,
                marker= {'color': 'mediumvioletred',
                         'line' :{ 'color': '#1C1C1C',
                                 'width': 3}},
                opacity = 0.6,
                name = 'Situação "Concluíida" em 2018') 
       ]


conf_layout2 = go.Layout(title= 'Projetos em situação "Concluída" por centro',
                   xaxis = {'title':'Centros'},
                   yaxis = {'title':'Quantidade'}
                    ) 


fig2a = go.Figure(data = data2, layout = conf_layout2)



data = [ go.Bar(x=dataset_2017.loc['Total'].index,
                y=dataset_2017.loc['Total'].values,
                marker= {'color': 'blue',
                         'line' :{ 'color': '#1C1C1C',
                                 'width': 3}},
                opacity = 0.5,
                name = 'Situação "Concluíida" em 2017')]
conf_layout = go.Layout(title= ' Projetos em situação "Concluída" por centro',
                   xaxis = {'title':'Centros'},
                   yaxis = {'title':'Quantidade'})
figa = go.Figure(data = data, layout = conf_layout)


data3 = [ go.Bar(x=dataset_2019.loc['Total'].index,
                 y=dataset_2019.loc['Total'].values,
                 marker= {'color': 'lawngreen',
                         'line' :{ 'color': '#1C1C1C',
                                 'width': 3}},
                opacity = 0.6,
                name = 'Situação "Em Execução" em 2019')]
conf_layout3 = go.Layout(title= 'Projetos com situação "Em Execução" por centro',
                   xaxis = {'title':'Centros'},
                   yaxis = {'title':'Quantidade'}) 
fig3a = go.Figure(data = data3, layout = conf_layout3)


trace = go.Pie(labels = dataset_2017.loc['Total'].index,
               values = dataset_2017.loc['Total'].values,
               direction = 'clockwise')

layout = go.Layout(title = 'Percentagem de projetos em situação "Concluída" por centro em 2017') 
pie1 = go.Figure(data = trace, layout = layout)


trace2 = go.Pie(labels = dataset_2018.loc['Total'].index,
               values = dataset_2018.loc['Total'].values,
               direction = 'clockwise')
layout2 = go.Layout(title = 'Percentagem de projetos em situação "Concluída" por centro em 2018') 
pie2 = go.Figure(data = trace2, layout = layout2)


trace3 = go.Pie(labels = dataset_2019.loc['Total'].index,
               values = dataset_2019.loc['Total'].values,
               direction = 'clockwise')
layout3 = go.Layout(title = 'Percentagem de projetos em situação "Em Execução" por centro em 2019') 
pie3 = go.Figure(data = trace3, layout = layout3)



def manu():
    layout = html.Div([
    nav,
    html.H1(children='Observatório de dados  - Ano 2',
            style={
            'color': '#191970',
            'textAlign': 'center'
        }),

    html.Div(children = [
        html.H5(children='Veja algumas informações sobre os projetos de extenção no periódo de 2017-2019',
                style={
                'textAlign': 'center',
                'color': '#1C1C1C'
            }),
    ],style={'marginBottom': 50, 'marginTop': 35,'background':'#F5DEB3'}),

    html.Div(children = [
        html.P('Escolha um ano abaixo',style = {'fontSize': 23}),
        dcc.RadioItems(id = 'years',
            options=[
            {'label': '2017', 'value': '17'},
            {'label': '2018', 'value':'18'},
            {'label': '2019', 'value':'19'}
            ],
            value = '17',
            labelStyle={'display': 'inline-block'})
        ]),

    html.Div(children=[
        html.Div(
            dcc.Graph(id='bar_graph',),className = 'six columns'
        ),
        html.Div(
            dcc.Graph (id = 'pie_graph'),className = 'six columns'
        )
    ],className = 'one row')
    ])
    return layout

