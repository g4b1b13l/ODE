import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from mapa import grupos,dados,dict_csv,state_data,geo_data,base,dict_centros,dict_coordenadas,folder, extension, separator,files_logos, folder_1,files_json,folder_2,files_dados,tooltip,html1,limpa_nome_arquivo_json,limpa_nome_arquivo,gera_cloropleth,gera_camadas_ufpb,gera_icones_da_ufpb,mapa_da_ufpb,mapa
from joao import fig1, fig2, joao
from rafael import fig_1,fig_2,fig_3,rafael 
from manu import manu, figa,fig2a,fig3a,pie1,pie2,pie3   
from homepage import Homepage
import folium  
from folium import IFrame, FeatureGroup 

app =  dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED],     
        meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}         
    ])
        
app.config.suppress_callback_exceptions = True   

app.layout = html.Div([ 
dcc.Location(id = 'url', refresh = False),      
html.Div(id = 'page-content')
])


@app.callback(Output('page-content', 'children'),     
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/mapa-ufpb':
        return mapa()
    if pathname == '/joao':
        return joao()
    if pathname == '/rafael':
        return rafael()            
    if pathname == '/emmanuela':       
        return manu()           
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
    return open('Apoio\\mapa_ufpb_centros.html', 'r').read()

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
    app.run_server(debug=True,use_reloader=False,port=1530)                     






