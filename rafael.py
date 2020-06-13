import pandas as pd
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#init_notebook_mode(connected=True)

import dash
import dash_core_components as dcc
import dash_html_components as html


from navbar import Navbar



nav = Navbar()

#dados = pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\Atividade Rafael\\contagem')    
#dados2 = pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\Atividade Rafael\\relacao') 

dados = pd.read_csv('Apoio\\contagem')    
dados2 = pd.read_csv('Apoio\\relacao') 


fig_1 = make_subplots(rows=1, cols=1,row_titles = ['Quantidade de Membros'],  shared_yaxes=True)

fig_1.add_trace(go.Bar(x=['2017','2018','2019'], y=dados[(dados.index%2)==0]['descricao'].to_list(), name='DISCENTE'),1,1)
fig_1.update_layout(coloraxis=dict(colorscale='Bluered'), showlegend=False)
fig_1.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))
fig_1.update_layout(title_text='Discentes e Docentes Evolvidos com Extensão nos Anos de 2017, 2018 e 2019', title_x=0.5)

fig_1.add_trace(go.Bar(x=['2017','2018','2019'], y=dados[(dados.index%2)!=0]['descricao'].to_list(), name='DOCENTE'),1,1)
fig_1.update_layout(coloraxis=dict(colorscale='Bluered'), showlegend=True)
fig_1.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))






fig_2 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]], subplot_titles=['2017', '2018','2019'])
fig_2.update_layout(autosize=True)#,width=990,height=400)
fig_2.update_traces(textposition='inside')
#fig2.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig_2.add_trace(go.Pie(labels=['DISCENTE','DOCENTE'], values=dados['descricao'].loc[:1], textinfo='label+percent', name='2017'),1, 1)
fig_2.add_trace(go.Pie(labels=['DISCENTE','DOCENTE'], values=dados['descricao'].loc[2:3], textinfo='label+percent', name='2018'),1, 2)
fig_2.add_trace(go.Pie(labels=['DISCENTE','DOCENTE'], values=dados['descricao'].loc[4:], textinfo='label+percent', name='2019'),1, 3)
fig_2.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))
fig_2.update_layout(title_text='Percentual de Discentes e Docentes nos Anos de 2017, 2018 e 2019', title_x=0.5)



dados2[['2017','2018','2019']] = dados2[['2017','2018','2019']].applymap(lambda x : "%.2f" % x)


fig_3 = make_subplots(rows=1, cols=1,row_titles = ['Razão Alunos/Professores'],  shared_yaxes=True)

fig_3.add_trace(go.Bar(x=dados2['centro'].to_list(), y= dados2['2017'].to_list(), name='2017',text=dados2['2017'].to_list(), textposition='auto',),1,1)
fig_3.update_layout(coloraxis=dict(colorscale='Bluered'), showlegend=False)      
fig_3.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))
fig_3.update_layout(title_text='Razão entre Discentes e Docentes por Centro nos Anos de 2017, 2018 e 2019', title_x=0.5)

fig_3.add_trace(go.Bar(x=dados2['centro'], y=dados2['2018'].to_list(), name='2018',text=dados2['2018'].to_list(), textposition='auto',),1,1)
fig_3.update_layout(coloraxis=dict(colorscale='Bluered'), showlegend=True)
fig_3.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))

fig_3.add_trace(go.Bar(x=dados2['centro'], y=dados2['2019'].to_list(), name='2019',text=dados2['2019'].to_list(), textposition='auto',),1,1)
fig_3.update_layout(coloraxis=dict(colorscale='Bluered'), showlegend=True)
fig_3.update_traces(marker=dict(line=dict(color='#000000', width=0.5)))



def rafael():
    layout = html.Div([
    nav,
    html.H1('Escolha abaixo qual é a figura que você quer exibir : ',style={'textAlign': 'center', 'margin-top': '15px','margin-bottom': '15px'}),
    dcc.Dropdown(
        id='dropdown-rafael',   
        options=[{'label': i, 'value': i} for i in ['Figura1', 'Figura2','Figura3']], #cria um dropdown (caixa de seleção) com os elementos passados na lista
        value='LA'
    ),
    html.Div(id='graf-rafael',style={'display': 'inline-block','width': '100%'}),    
    html.Br(),
    html.Br(),
    html.P([html.Br()],'linebreak?'), #Pula uma linha 
    ])
    return layout




