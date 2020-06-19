import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


from navbar import Navbar


nav = Navbar()

#df_2017 = pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\Atividade JOao\\Atividade4\\df_2017.csv',index_col=0)
#df_2018 = pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\Atividade JOao\\Atividade4\\df_2018.csv',index_col=0)

all_options = {
    'João Guilherme': ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4', 'Semana 5'],
    'Emmanuela': ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4', 'Semana 5'],
    'Gabriel': ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4', 'Semana 5'],
    'Rafael': ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4', 'Semana 5']
    
}
body = html.Div([
    html.H1('Página das Reuniões', style={'textAlign': 'center'}), #Cria um texto de título
    html.H2('Lista de Tarefas Desenvolvidas', style={'font-size':26, 'textAlign': 'left'}), #Cria um texto de título
    html.P('Selecione o Discente:', style={'font-size':18,'textAlign': 'left'}), #Cria um texto de título
    
    dcc.Dropdown(
        id='countries-dropdown',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value= 'João Guilherme'
    ),

    html.Div(html.P(html.Br())), #Pula uma linha
    html.P('Selecione a Semana de Trabalho:', style={'font-size':18,'textAlign': 'left'}), #Cria um texto de título

    dcc.Dropdown(id='cities-dropdown'),

    html.Hr(),

    html.Div(id='display-selected-values')
])

def relatorio():
    layout = html.Div([
    nav,
    body
    ])
    return layout

