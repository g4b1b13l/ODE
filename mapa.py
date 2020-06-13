import dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
from dash.dependencies import Input, Output
import plotly.offline as py
from plotly.graph_objs import *
import plotly.graph_objs as go 
import dash_bootstrap_components as dbc
import folium  
from folium import IFrame, FeatureGroup 
     
import os  
import base64 
import glob  
import pandas as pd 
from folium.plugins import MarkerCluster   


### Data
import pandas as pd
import pickle
### Graphing
import plotly.graph_objects as go
### Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
## Navbar
from navbar import Navbar


nav = Navbar()    

retval = os.getcwd()


grupos = ['Grupo 1','Grupo 2','Grupo 3'] 
dados = ['Quantidade de projetos em 2017','Quantidade de projetos em 2018'] 

dict_csv = { 'Quantidade de projetos em 2017' : 'Projetos_2017.csv',
            'Quantidade de projetos em 2018' : 'Projetos_2018.csv'   
    
}



#state_data=pd.read_csv('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\dados\\projetos_2017.csv', engine='python')
#geo_data = 'C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\ufpb_centros.json'   

state_data=pd.read_csv('Apoio\\projetos_2017.csv', engine='python')
geo_data = 'Apoio\\ufpb_centros.json'  


base = 'Centros incluidos no Polígono: '      

dict_centros = {   
    'poligono_1': base + 'CCHLA, CEAR, CCSA, CE',
    'poligono_2': base + 'CCJ, CT',
    'poligono_3': base + 'CBIOTEC',   
    'poligono_4': base + 'CCTA',   
    'poligono_5': base + 'CCEN',           
    'poligono_6': base + 'CCS',   
    'poligono_7': base + 'CCM',
    'outros': 'Não existem centros incluidos nesse Polígono'  

    
} 

dict_coordenadas = {
    'cbiotec' : [-7.140993, -34.846455],
    'ccen'  : [-7.139640, -34.845020],    
    'cchla' : [-7.139370, -34.850374], 
    'ccj' :  [-7.141978, -34.848935], 
    'ccm' : [-7.136423, -34.840567 ],    
    'ccs' :  [-7.135673, -34.841516],  
    'ccsa' :  [-7.141069, -34.849936],   
    'ccta' : [-7.137422, -34.849572],  
    'ce' : [-7.139994, -34.850124],  
    'cear' : [-7.141625, -34.850556],  
    'ct' : [-7.142505, -34.850309]    
} 

#folder ='C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\logos'    
folder ='Apoio\\logos'    

extension = '*'                               
separator = ','                                    
extension = '*.' + extension  
os.chdir(folder)             
files_logos= glob.glob(extension)   

os.chdir(retval)             

#folder_1 ='C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\arquivos_json' 
#folder_1 ='C:Apoio\\arquivos_json' 
folder_1='Apoio\\arquivos_json'
os.chdir(folder_1)             
files_json= glob.glob(extension)   
os.chdir(retval)             

#folder_2 ='C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\dados' 
folder_2 ='Apoio\\dados' 
os.chdir(folder_2)             
files_dados= glob.glob(extension)   
os.chdir(retval)             

tooltip = "Clique para abrir a imagem"     
html1 = '<img src="data:image/png;base64,{}">'.format  

def limpa_nome_arquivo_json(logo):   
    files=logo.replace('json','')      
    files=files.replace('.','') 
    return files 

def limpa_nome_arquivo(logo):  
    files=logo.replace('jpeg','')      
    files=files.replace('jpg','')  
    files=files.replace('png','')  
    files=files.replace('.','') 
    return files 

def gera_cloropleth(geo_data,state_data,files_dados,mapa_,dado,grupos):   

    if 'Grupo 1' in grupos:
        state_data_1=pd.read_csv(dict_csv[dado], engine='python')
        #geo_data = 'C:\\Users\\Pessoal\\Desktop\\ODE\\choropleth\\gp_1.json'
        geo_data = 'Apoio\\choropleth\\gp_1.json'        
        filtered = ['poli2','poli3']
        state_data_1 = state_data_1[state_data_1['poligono'].isin(filtered)]
    if 'Grupo 2' in grupos:
        state_data_1=pd.read_csv(dict_csv[dado], engine='python') 
        #geo_data = 'C:\\Users\\Pessoal\\Desktop\\ODE\\choropleth\\gp_2.json'
        geo_data = 'Apoio\\choropleth\\gp_2.json'

        filtered = ['poli1','poli4','poli9','poli10'] 
        state_data_1 = state_data_1[state_data_1['poligono'].isin(filtered)]
    if 'Grupo 3' in grupos:  
        state_data_1=pd.read_csv(dict_csv[dado], engine='python')       
        #geo_data = 'C:\\Users\\Pessoal\\Desktop\\ODE\\choropleth\\gp_3.json'
        geo_data = 'Apoio\\choropleth\\gp_3.json'

        filtered = ['poli5','poli6','poli7','poli11','poli12','poli13'] 
        state_data_1 = state_data_1[state_data_1['poligono'].isin(filtered)]   
    if 'Grupo 1' in grupos and 'Grupo 2' in grupos:
        state_data_1=pd.read_csv(dict_csv[dado], engine='python')
        #geo_data = 'C:\\Users\\Pessoal\\Desktop\\ODE\\choropleth\\gp_12.json'

        geo_data = 'Apoio\\choropleth\\gp_12.json'
        filtered = ['poli2','poli3','poli1','poli4','poli9','poli10']
        state_data_1 = state_data_1[state_data_1['poligono'].isin(filtered)]
    if 'Grupo 1' in grupos and 'Grupo 3' in grupos:
        state_data_1=pd.read_csv(dict_csv[dado], engine='python')
        #geo_data = 'C:\\Users\\Pessoal\\Desktop\\ODE\\choropleth\\gp_13.json'

        geo_data = 'Apoio\\choropleth\\gp_13.json'
        filtered = ['poli2','poli3','poli5','poli6','poli7','poli11','poli12','poli13']
        state_data_1 = state_data_1[state_data_1['poligono'].isin(filtered)]
    if 'Grupo 2' in grupos and 'Grupo 3' in grupos:
        state_data_1=pd.read_csv(dict_csv[dado], engine='python')
        #geo_data = 'C:\\Users\\Pessoal\\Desktop\\ODE\\choropleth\\gp_23.json'

        geo_data = 'Apoio\\choropleth\\gp_23.json'
        filtered = ['poli1','poli4','poli9','poli10','poli5','poli6','poli7','poli11','poli12','poli13']
        state_data_1 = state_data_1[state_data_1['poligono'].isin(filtered)]
    if 'Grupo 1' in grupos and 'Grupo 2' in grupos and 'Grupo 3' in grupos:
        state_data_1 = pd.read_csv(dict_csv[dado], engine='python')
        #geo_data = 'C:\\Users\\Pessoal\\Desktop\\ODE\\choropleth\\ufpb_centros.json'
        geo_data = 'Apoio\\choropleth\\ufpb_centros.json'

    folium.Choropleth(   
                geo_data = geo_data, 
                name='Choropleth',
                data=state_data_1,    
                columns=['poligono', 'qtd_projeto'],   
                key_on='feature.id', 
                fill_color='YlGn',    
                fill_opacity=0.7,   
                line_opacity=0.2,
                legend_name='Quantidade de projetos',   
                #show=False,
                #overlay=False         
            ).add_to(mapa_)   
        
        
    #folium.LayerControl().add_to(map)
  

def gera_camadas_ufpb(arquivo_json,mapa_):    
    #AQUIII

    #camadas_ufpb = os.path.join('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\arquivos_json\\' + arquivo_json)
    camadas_ufpb = os.path.join('Apoio\\arquivos_json\\' + arquivo_json)

    arquivo_json=limpa_nome_arquivo_json(arquivo_json)
    camada=folium.GeoJson(camadas_ufpb,name=arquivo_json).add_to(mapa_)    
    flag = arquivo_json.replace('poligono_', '')    
    if int(flag) > 7: 
        arquivo_json = 'outros'
    camada.add_child(folium.Popup(dict_centros[arquivo_json]))
    camada.add_to(mapa_)    

def gera_icones_da_ufpb(logo,dict_logo,dict_coordenadas,html1,tooltip,mapa_):
    #AQUIII
    #picture1 = base64.b64encode(open('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\logos\\' + logo ,'rb').read()).decode()

    picture1 = base64.b64encode(open('Apoio\\logos\\' + logo ,'rb').read()).decode()
    iframe1 = IFrame(html1(picture1), width=300, height=300)   
    #icon1 = folium.features.CustomIcon('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\logos\\' + logo, icon_size=(20,20))
    icon1 = folium.features.CustomIcon('Apoio\\logos\\' + logo, icon_size=(20,20))
    
    files=limpa_nome_arquivo(logo)   
    popup1 = folium.Popup(iframe1,max_width=650)       
    folium.Marker(location=dict_coordenadas[files],popup= popup1, tooltip=tooltip,icon=icon1).add_to(mapa_)
    
def mapa_da_ufpb(tooltip, files_logos,dict_coordenadas,files_json,geo_data,state_data, files_dados,mapa_,flag,grupos,dado):
    files_json = []   
    files_logos = []    



    if 'Grupo 1' in grupos:
        files_json.extend(['poligono_2.json','poligono_3.json', 'poligono_8.json'])
        files_logos.extend([ 'ccj.png', 'ct.jpg', 'cbiotec.png',])    
    if 'Grupo 2' in grupos:
        files_json.extend(['poligono_1.json', 'poligono_4.json', 'poligono_9.json' , 'poligono_10.json'])
        files_logos.extend(['cchla.png',  'cear.jpg',  'ccsa.jpg',  'ce.jpg',  'ccta.jpeg',])
    if 'Grupo 3' in grupos:
        files_json.extend(['poligono_5.json' ,  'poligono_6.json' , 'poligono_7.json' ,  'poligono_11.json' , 'poligono_12.json' , 'poligono_13.json'])   
        files_logos.extend([ 'ccen.png',  'ccs.jpg',  'ccm.jpg'])   
    if flag == 'nao': 
        for arquivo_json in files_json:
            gera_camadas_ufpb(arquivo_json,mapa_)  
    for logo in files_logos:    
        gera_icones_da_ufpb(logo,logo,dict_coordenadas,html1,tooltip,mapa_)
    if flag == 'sim':    
        gera_cloropleth(geo_data,state_data,files_dados,mapa_,dado,grupos)    
    #mapa_.save("C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\mapa_ufpb_centros.html") 
    mapa_.save("Apoio\\mapa_ufpb_centros.html") 




def mapa():
    layout = html.Div([
    nav,
	html.Label('Escolha o grupo desejado'), 
    dcc.Dropdown(
    	id = 'grupos',  
        options=[
            {'label': j, 'value': j} for j in grupos  
        ],
        value=['Grupo 1','Grupo 2','Grupo 3'],   
         multi=True,
         style={'margin-bottom':'10px'}
    ),

    html.Label('Deseja analisar o modo Choropleth?'), 
    dcc.RadioItems(
                    options=[  
                        {'label': 'Sim', 'value': 'sim'},
                        {'label': 'Não', 'value': 'nao'},      

                    ],
                    id='flag',
                    value='nao',
                    labelStyle={'display': 'inline-block','margin-bottom':'10px'}   
                ),
    html.Div([
    html.Label('Escolha com deseja analisar os dados'), 
    dcc.Dropdown(
        id = 'dados',  
        options=[
            {'label': j, 'value': j} for j in dados  
        ],
        value=0,   
         multi=False,
         style={'margin-bottom':'10px'}

    ),],
    id='choropleth',
    style = {'display': 'none'}),



     #html.Iframe(id='mapa', srcDoc=open('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Pasta de backup\\ODE\\mapa_ufpb_centros.html', 'r').read(), width='100%', height='430'),  

     html.Iframe(id='mapa', srcDoc=open('Apoio\\mapa_ufpb_centros.html', 'r').read(), width='100%', height='430'),  
    ])
    return layout





