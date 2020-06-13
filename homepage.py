import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from navbar import Navbar
import base64
from dash.dependencies import Output, Input, State
nav = Navbar()


ufpb_image = base64.b64encode(open('Apoio\\foto_ode.png', 'rb').read())


body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("Quem somos?"),
                     html.P(
                         """\
A extensão universitária é uma ferramenta de promoção do desenvolvimento social e de difusão do conhecimento dentro e fora da universidade. Muitas são as ações desenvolvidas na UFPB com este objetivo. No que concerne a gerência dessas ações, ainda, existem poucas ferramentas sendo implementadas para avaliar dados gerados e permitir um acompanhamento de tais atividades de forma quantitativa. A proposta submetida, é uma opção para permitir uma visão mais quantitativa dos dados criados por meio dessas ações. Usando ferramentas de análise de dados e propondo métricas que auxiliam a gestão das ações de extensão dentro da UFPB, por meio da PRAC ou mesmo das Assessorias de Extensão. Esta iniciativa, agora em seu segundo ano, é batizada de Observatório de Dados da Extensão, e forneceu informações estratégicas para um melhor conhecimento das ações de extensão desenvolvidas na UFPB."""
                           ),
                           dbc.Button("Versão", color="secondary",id='popover_target'),    
                           dbc.Popover(
            [
                dbc.PopoverHeader("Ultima Atualização"),
                dbc.PopoverBody("V.0.1, 08/06/2020"),
            ],
            id="popover",
            is_open=False,
            target="popover_target",
            placement='top'
        ),   

                   ],
                  md=4,
               ),
              dbc.Col(
                 [

                html.Img(id='img_logo_ufpb',height='auto'
                        ,src='data:image/png;base64,{}'.format(ufpb_image.decode())
                        ,style={'display': 'block','height':'480px','position':'absolute','left':'50px','top':'10px'}
                        ),
                        ]
                     ),
                ]
            )
       ],
className="mt-4",
)


def Homepage():
    layout = html.Div([
    nav,
    body
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Homepage() 
suppress_callback_exceptions=True





if __name__ == "__main__":
    app.run_server(debug=True,use_reloader=False,port=1216)   



