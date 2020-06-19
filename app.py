import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from mapa import grupos,dados,dict_csv,state_data,geo_data,base,dict_centros,dict_coordenadas,folder, extension, separator,files_logos, folder_1,files_json,folder_2,files_dados,tooltip,html1,limpa_nome_arquivo_json,limpa_nome_arquivo,gera_cloropleth,gera_camadas_ufpb,gera_icones_da_ufpb,mapa_da_ufpb,mapa
from joao import fig1, fig2, joao
from rafael import fig_1,fig_2,fig_3,rafael 
from manu import manu, figa,fig2a,fig3a,pie1,pie2,pie3 
from relatorio import all_options, relatorio  
from homepage import Homepage
from quem_somos import quem_somos
import folium  
from folium import IFrame, FeatureGroup 
from flask import Flask
from login import app as server
app =  dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED],server=server,url_base_pathname='/app1/',
        meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}         
    ])

from logging import FileHandler, WARNING



app.config.suppress_callback_exceptions = True   

app.layout = html.Div([ 
dcc.Location(id = 'url', refresh = False),      
html.Div(id = 'page-content')
])



@app.callback(Output('page-content', 'children'),     
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/mapa-ufpb':
        print(pathname,flush=True)
        return mapa()
    if pathname == '/joao':
        return joao()
    if pathname == '/rafael':
        return rafael()            
    if pathname == '/emmanuela':       
        return manu() 
    if pathname == '/relatorio':       
        return relatorio()
    if pathname == '/quemsomos':       
        return quem_somos()
    return Homepage()

@app.callback(
   dash.dependencies.Output('choropleth', 'style'),
    [dash.dependencies.Input('flag', 'value')])             

def some_o_grafico_para_aparecer_os_outros(valor):
    if valor == 'nao':
        return {'display': 'none'}
    if valor == 'sim':
        return {'display': 'block'} 
    else:
        return {'display': 'none'}         

@app.callback(
   dash.dependencies.Output('dados', 'value'),
    [dash.dependencies.Input('flag', 'value')])             

def some_o_grafico_para_aparecer_os_outros(valor):
    if valor == 'nao':
        return 0
    else:
        return dash.no_update

@app.callback(
    dash.dependencies.Output('mapa', 'srcDoc'),
    [dash.dependencies.Input('grupos', 'value'),
    dash.dependencies.Input('dados', 'value'),
    dash.dependencies.Input('flag', 'value')])

def update_map(grupos,dado,flag):
    mapa_ = folium.Map(location= [-7.1385,-34.8464], zoom_start=15,tiles='cartodbpositron')     
    mapa_da_ufpb(tooltip, files_logos,dict_coordenadas,files_json,geo_data,state_data, files_dados,mapa_,flag,grupos,dado)  
    #return open('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\mapa_ufpb_centros.html', 'r').read()
    return open('Apoio/mapa_ufpb_centros.html', 'r').read()  

####################mapa###########


@app.callback(dash.dependencies.Output('page-1-content', 'children'), #Recupea o dropdown informado
              [dash.dependencies.Input('page-1-dropdown', 'value')])


def page_1_dropdown(value): #Faz a operação de 'Mostrar' a imagem dependendo do dropdown selecionado   
    if value == 'Figura1':
        return dcc.Graph(figure=fig1)    
    elif value == 'Figura2':
        return dcc.Graph(figure=fig2)   

##########joao-manu##############

@app.callback(dash.dependencies.Output('graf-rafael', 'children'), #Recupea o dropdown informado
              [dash.dependencies.Input('dropdown-rafael', 'value')])


def page_1_dropdown(value): #Faz a operação de 'Mostrar' a imagem dependendo do dropdown selecionado
    if value == 'Figura1':
        return dcc.Graph(figure=fig_1)
    if value == 'Figura2':
        return dcc.Graph(figure=fig_2)   
    if value == 'Figura3':
        return dcc.Graph(figure=fig_3)   
##########rafel##############


@app.callback([dash.dependencies.Output('bar_graph','figure'),
               dash.dependencies.Output('pie_graph','figure')],
               [dash.dependencies.Input('years','value')])


def update_graph(values):
    datas = []
    layouts=[]
    if '17' ==values:
        return figa,pie1

    elif '18' == values :
        return fig2a,pie2
        
    elif '19'== values:
        return fig3a,pie3



##########manu##############     

####exibirnotecomeça######

@app.callback(
    dash.dependencies.Output('cities-dropdown', 'options'),
    [dash.dependencies.Input('countries-dropdown', 'value')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

@app.callback(
    dash.dependencies.Output('cities-dropdown', 'value'),
    [dash.dependencies.Input('cities-dropdown', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('countries-dropdown', 'value'),
     dash.dependencies.Input('cities-dropdown', 'value')])
def set_display_children(selected_country, selected_city):
    if selected_country == 'João Guilherme' and selected_city=='Semana 1':
        return   html.Div([
        dcc.Markdown('''
        #### Atividades 11/05/2020 - 18/05/2020
        Criar um jupyter notebook para totalizar o numero de projetos: 
        - Ler arquivo dos dados (Anexo projetos_extensao_probex.csv)
        - Fazer a correção dos caracteres indesejados
        - Eliminar as duplicidades dos projetos existentes
        - Levantar os quantitativos dos projetos por ano (2017, 2018, 2019)(Situação em 2017 e 2018: Concluido / em 2019 Situação: Em Execução)
        Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
       html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14, 'textAlign':'center',  'color':'blue'}),  href='https://drive.google.com/drive/u/1/folders/1sXbVE5rI3HHmoSCsZlp1peDXNunYusCQ')
       
       
        ])
    
    elif selected_country == 'João Guilherme' and selected_city=='Semana 2':
        return   html.Div([ 
        dcc.Markdown('''
        #### Atividades 18/05/2020 - 25/06/2020
       Criar um jupyter notebook para listar as possíveis situações de cada projeto, por ano e por centro 
       - Ler arquivo dos dados (Anexo)
       - Fazer a correção dos caracteres indesejados
       - Eliminar as duplicidades dos projetos existentes
       - Levantar quais os tipos de situação que os projetos podem assumir
       - Quantas são as ocorrências por situação? (2017, 2018, 2019)
       - Quantitativos dos projetos por Unidade Proponente
       - Contagem de projetos com situação CONCLUÍDA em 2017 e 2018 separado por Centro,
       
       ListaCentros = ['CCS -','CEAR -','CCEN -','CT -','CCM -','CBIOTEC -','CTDR -','CCHLA -','CCTA -','CCHSA -','CCSA -','CI -','CCAE -','CCJ -','CCA -','CE -'],
       
       Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
            
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1_phDurzEtghAce9eb0Mb3IUpvGvFvyCr')
            
        ])    
            
    
    elif selected_country == 'João Guilherme' and selected_city=='Semana 3':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 25/05/2020 - 01/06/2020
        - Apresentar os dados obtidos anteriormente usando graficos (Pizza e Barra) 
        - Ordenar do menor para o maior numero de ocorrências
        Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
         html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1F3wBOrpy2QvS0dMRyvKIRdpCz4AwH1J-')
        ])
        
    elif selected_country == 'João Guilherme' and selected_city=='Semana 4':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 01/06/2020 - 08/06/2020
        - Criar Page com os graficos gerados
        - Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/19MhFt9rHR1ZyBedYp2ZDnSFgr5tEvocH')
            
        ])
        
    elif selected_country == 'João Guilherme' and selected_city=='Semana 5':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 08/06/2020 - 15/06/2020
        -  Page das reuniões (Atividades + Resultados)
        - Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1wZESu4ah1c-MSNBpoZ1vR-IYW63swQ2G')
              
        ])
    
    #Emmanuela
    
    elif selected_country == 'Emmanuela' and selected_city=='Semana 1':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 11/05/2020 - 18/05/2020
        Criar um jupyter notebook para totalizar o numero de projetos: 
        - Ler arquivo dos dados (Anexo projetos_extensao_probex.csv)
        - Fazer a correção dos caracteres indesejados
        - Eliminar as duplicidades dos projetos existentes
        - Levantar os quantitativos dos projetos por ano (2017, 2018, 2019)(Situação em 2017 e 2018: Concluido / em 2019 Situação: Em Execução)
        Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
            
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1TIn1lq4H4ji8nq3XqDMdabrua-xQYhTn')
        ]),
            
            
    elif selected_country == 'Emmanuela' and selected_city=='Semana 2':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 18/05/2020 - 25/06/2020
       Criar um jupyter notebook para listar as possíveis situações de cada projeto, por ano e por centro 
       - Levantar quais os tipos de situação que os projetos podem assumir
       - Quantas são as ocorrências por situação? (2017, 2018, 2019)
       - Quantitativos dos projetos por Unidade Proponente
       - Contagem de projetos com situação CONCLUÍDA em 2017 e 2018 separado por Centro,
       
       ListaCentros = ['CCS -','CEAR -','CCEN -','CT -','CCM -','CBIOTEC -','CTDR -','CCHLA -','CCTA -','CCHSA -','CCSA -','CI -','CCAE -','CCJ -','CCA -','CE -'],
       
       Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1TIn1lq4H4ji8nq3XqDMdabrua-xQYhTn')
            
        ])
    
    elif selected_country == 'Emmanuela' and selected_city=='Semana 3':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 25/05/2020 - 01/06/2020
        - Apresentar os dados obtidos anteriormente usando graficos (Pizza e Barra) 
        - Ordenar do menor para o maior numero de ocorrências
        Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
            
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1TIn1lq4H4ji8nq3XqDMdabrua-xQYhTn')
        ])
        
    elif selected_country == 'Emmanuela' and selected_city=='Semana 4':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 01/06/2020 - 08/06/2020
        - Criar Page com os graficos gerados
        - Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1TIn1lq4H4ji8nq3XqDMdabrua-xQYhTn')
        ])
        
    elif selected_country == 'Emmanuela' and selected_city=='Semana 5':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 08/06/2020 - 15/06/2020
        -  Page das reuniões (Atividades + Resultados)
        - Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1TIn1lq4H4ji8nq3XqDMdabrua-xQYhTn')
        ])
    
    #Gabriel
    
    elif selected_country == 'Gabriel' and selected_city=='Semana 1':
        return html.Div([ 
        dcc.Markdown('''
        #### Atividades 11/05/2020 - 18/05/2020
        Cria um jupyter notebook para gerar um mapa com os centros da UFPB
        - Gerar um json com a delimitação dos centros 
            *http://www.ccs.ufpb.br/cfisio/contents/imagens/mapa-do-campus-i-ufpb.jpg/view (Reproduzir essa informação)
            *http://geojson.io/#map=2/20.0/0.0
        - Construir o mapa baseado no folium com uma camada paracada centro
        
        Apresentar Resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1FSskOJ8HykDyKmymrF8QtrVA-4BkZ1tT')
            
        ])
    
    
    elif selected_country == 'Gabriel' and selected_city=='Semana 2':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 18/05/2020 - 25/06/2020
       Cria um jupyter notebook para gerar um mapa com os centros da UFPB
       - colorir o mapa de acordo com o dado
       - adicionar o evento click (Revelar a lista de centros presente no poligono)
       
       Apresentar Resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1FSskOJ8HykDyKmymrF8QtrVA-4BkZ1tT')
            
        ])
    
    elif selected_country == 'Gabriel' and selected_city=='Semana 3':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 25/05/2020 - 01/06/2020
        - Introduzir o conveito de filtro no mapa
        -dividir o conjunto de centros em 3 grupos
        -cada grupo pode ser escolhido individualmente em um listbox
        -uma vez escolhido o grupo, o grafico deve fazer o highlight apenas nos centros do grupo escolhido
        - Criar pastas compartilhadas
        
        Apresentar Resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1FSskOJ8HykDyKmymrF8QtrVA-4BkZ1tT')
        ])
        
    elif selected_country == 'Gabriel' and selected_city=='Semana 4':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 01/06/2020 - 08/06/2020
        - Fazer o Exemplo Multipage dash
        
        Apresentar Resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1FSskOJ8HykDyKmymrF8QtrVA-4BkZ1tT')
        ])
        
    elif selected_country == 'Gabriel' and selected_city=='Semana 5':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 08/06/2020 - 15/06/2020
        - Heroku 
        - Github 
        - Pasta de Apoio
        - Root
        
        Apresentar Resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1FSskOJ8HykDyKmymrF8QtrVA-4BkZ1tT')
        ])  
    
    #Rafael
    
    elif selected_country == 'Rafael' and selected_city=='Semana 1':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 11/05/2020 - 18/05/2020
        Criar um jupyter notebook para totalizar o numero de participantes 
        - Ler arquivo dos dados (Anexo membros_projetos_extensão_probex.csv)
        - Fazer a correção dos caracteres indesejados
        - Eliminar, eventual, duplicidade de docentes e discentes existentes / id_projeto
        - Levantar os quantitativos dos docentes e discentes por ano (2017, 2018, 2019)
        
        Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
            
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1izgCAjsdvjp5ABunuFBluyt4zxMZTxWE')
        
        ])
    
    elif selected_country == 'Rafael' and selected_city=='Semana 2':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 18/05/2020 - 25/06/2020
       - Quais são as ocorrências por categoria de aluno?
       - Quantitativos dos alunos por Curso? (2017, 2018, 2019)
       - Quais são as ocorrências por categoria de docente?
       - Quantitativos dos docentes por departamento (2017, 2018, 2019)
       
       Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1izgCAjsdvjp5ABunuFBluyt4zxMZTxWE')
        ])
    
    elif selected_country == 'Rafael' and selected_city=='Semana 3':
        return html.Div([ 
        dcc.Markdown('''
        #### Atividades 25/05/2020 - 01/06/2020
        - Corrigir os comentarios das celulas nos notebooks
        - Listar projetos que possuem apenas docentes (2017/2018 Concluídos, 2019 Em Execução)(2017, 2018, 2019)
        - Calcular a relação alunos/professor para cada centro  (2017, 2018, 2019)
        
        Apresentar Resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1izgCAjsdvjp5ABunuFBluyt4zxMZTxWE')
        ])
        
    elif selected_country == 'Rafael' and selected_city=='Semana 4':
        return html.Div([ 
        dcc.Markdown('''
        #### Atividades 01/06/2020 - 08/06/2020
        - Gerar o gráfico de pizza e barra com os resultados
        - Criar Page com os graficos gerados
        
        Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1izgCAjsdvjp5ABunuFBluyt4zxMZTxWE')
        ])
        
    elif selected_country == 'Rafael' and selected_city=='Semana 5':
        return html.Div([
        dcc.Markdown('''
        #### Atividades 08/06/2020 - 15/06/2020
        - Apresentação Extensão
        
        Apresentar resultados
        ''', style={'horizontal-Align':'left', 'textAlign':'left'}),
        html.A(html.Button('Baixar notebook', id='btn1', n_clicks=0, autoFocus=True, style={'width':300,  'height':40, 'font-size':14,  'color':'blue', 'textAlign':'center'}),  href='https://drive.google.com/drive/u/1/folders/1izgCAjsdvjp5ABunuFBluyt4zxMZTxWE')
        ])



####exibir note_termina####

@app.callback(
    Output("popover", "is_open"),
    [Input("popover_target", "n_clicks")],
    [State("popover", "is_open")],
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open





if __name__ == '__main__':
	server.run(port=5048)   








