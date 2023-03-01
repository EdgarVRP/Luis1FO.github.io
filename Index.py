# -*- coding: utf-8 -*-
# import dash-core, dash-html, dash io, bootstrap
from html.entities import html5
from importlib.resources import contents
from dash import dcc,html
from dash.dependencies import Input, Output
# Dash Bootstrap components
import dash_bootstrap_components as dbc
# Navbar, layouts, custom callbacks
from layouts import planLayout,codLayout,consLayout,pruLayout,lanLayout,dspLayout,opLayout,monLayout
# Import app
from app import app
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "1rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "1rem 1rem",
}
sidebar = html.Div(
    [
        html.H2("Dashboard", className="display-5"),
        html.H2("DevOps", className="display-5"),
        html.Hr(),
        dbc.Nav(
            [dbc.NavItem(dbc.NavLink("Inicio",active="exact",href="/"))],
           vertical=True, 
           pills=True,
        ),
        html.Hr(),
        html.H2("Procesos DevOps", className="lead"),
        dbc.Nav(
            [
            dbc.NavItem(dbc.NavLink("Planeacion",active="exact",href="/plan")),
            dbc.NavItem(dbc.NavLink("Codificacion",active="exact",href="/cod")),
            dbc.NavItem(dbc.NavLink("Construccion",active="exact",href="/cons")),
            dbc.NavItem(dbc.NavLink("Pruebas",active="exact",href="/pru")),
            dbc.NavItem(dbc.NavLink("Lanzamiento",active="exact",href="/lan")),
            dbc.NavItem(dbc.NavLink("Despliegue",active="exact",href="/dsp")),
            dbc.NavItem(dbc.NavLink("Operacion",active="exact",href="/ope")),
            dbc.NavItem(dbc.NavLink("Monitoreo",active="exact",href="/mon")),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
content = html.Div(id="page-content", style=CONTENT_STYLE)
# Sidebar layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == '/':
         return html.Div(html.Img(src=app.get_asset_url('logo.png'))),html.Div([dcc.Markdown('''
            ### Introduccion 
            El objetivo de esta investigacion es proporcionar una herramienta de control que permitira a las empresas desarrolladoras de software,
            visualizar en forma grafica el estado de avance en el que se encuentran sus proyectos DevOps, permitiendo dar seguimiento, mostrar su continuidad
            y progreso a traves del tiempo.
           
            Para lograr el objetivo planteado, se desarrollo una herramienta de software con base en tecnologias de codigo abierto,
            utilizando los 8 procesos mas comunes del enfoque DevOps y apoyandose del estandar IEEE 2675 for DevOps
        ''')],className='home'),html.Img(src=app.get_asset_url('devops.png'))
    if pathname =='/plan':
        #return html.Div([dbc.Row(dbc.Col(html.Div("Proceso de Planificacion. En esta fase se definen los requisitos y valores empresariales. Indicador:Puntos de historia"))),]),html.Div(planLayout)
        return  '/',html.Div(planLayout)
    if pathname == '/cod':
        return html.Div(codLayout)
       # return  html.P("Proceso de Codificacion. Esta fase implica el diseño del software y la creacion del codigo. Indicador:Tasa de defectos"),codLayout
    if pathname == '/cons':
        return consLayout,html.P("Proceso Construccion o Compilacion. En esta fase se gestionan las versiones y las compilaciones del software"
                                 "se utilizan herramientas automatizadas que ayudan a compilar y crear paquetes de codigo para publicarlos posteriormente en un ambiente de produccion.Indicador:Tasa de defectos ")
    if pathname == '/pru':
        return html.P("Proceso de Pruebas. Esta fase incluye la realizacion de pruebas continuas (manuales o automatizadas)"
                      " para garantizar la calidad de la programacion. Indicador: "),pruLayout
    if pathname == '/lan':
        return  lanLayout, html.P("Proceso de Puesta en marcha o lanzamiento. En esta fase se emplean herramientas que ayudan a gestionar, coordinar, programar y automatizar las tareas de produccion de las versiones de productos. Indicador:")
    if pathname == '/dsp':
        return html.P("Proceso de Despliegue. En esta fase se realiza la publicacion ininterrumpida de cambios de codigo. Indicador: Frecuencia de despliegue"),dspLayout
    if pathname == '/ope':
        return opLayout, html.P("Proceso de Operacion o Funcionamiento. En esta fase se gestiona el software durante su produccion aqui se da soporte al software. Indicador:Tiempo medio de deteccion (MTTD)")
    if pathname == '/mon':
        #return html.P("Proceso de Supervision o monitoreo. En esta fase se identifica y recopila informacion sobre problemas que surgen en una version de software especifica que se encuentra en produccion. Indicador:Tiempo medio de recuperacion (MTTR)"),monLayout
        return  monLayout
    else:
        # If the user tries to reach a different page, return a 404 message
        return dbc.Alert(
        [
        html.H1("404: No encontrado", className="text-danger"),
        html.Hr(),
        html.P(f"La ruta {pathname} no fue reconocida..."),    
        html.A("Inicio", href="/", className="alert-link"),
        ]
        ),
# Call app server
if __name__ == '__main__':
    # set debug to false when deploying app
    app.run_server(debug=True)


    