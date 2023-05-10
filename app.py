import os
from dash import dcc, html
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from flask import Flask
from layouts import (
    planLayout,
    codLayout,
    consLayout,
    pruLayout,
    lanLayout,
    dspLayout,
    opLayout,
    monLayout,
)

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "DevOps"
srv = app.server
app.config.suppress_callback_exceptions = True


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "1rem 1rem",
    "background-color": "#f8f9fa",
}

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
            [dbc.NavItem(dbc.NavLink("Inicio", active="exact", href="/"))],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        html.H2("Procesos DevOps", className="lead"),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Planeacion", active="exact", href="/plan")),
                dbc.NavItem(dbc.NavLink("Codificacion", active="exact", href="/cod")),
                dbc.NavItem(dbc.NavLink("Construccion", active="exact", href="/cons")),
                dbc.NavItem(dbc.NavLink("Pruebas", active="exact", href="/pru")),
                dbc.NavItem(dbc.NavLink("Lanzamiento", active="exact", href="/lan")),
                dbc.NavItem(dbc.NavLink("Despliegue", active="exact", href="/dsp")),
                dbc.NavItem(dbc.NavLink("Operacion", active="exact", href="/ope")),
                dbc.NavItem(dbc.NavLink("Monitoreo", active="exact", href="/mon")),
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
    if pathname == "/":
        return html.Div(
            [
                html.Img(src=app.get_asset_url("logo.png")),
                html.Div(
                    [
                        dcc.Markdown(
                            """
            ### Introduccion 
            El objetivo de esta investigacion es proporcionar una herramienta de control que permitira a las empresas desarrolladoras de software,
            visualizar en forma grafica el estado de avance en el que se encuentran sus proyectos DevOps, permitiendo dar seguimiento, mostrar su continuidad
            y progreso a traves del tiempo.
           
            Para lograr el objetivo planteado, se desarrollo una herramienta de software con base en tecnologias de codigo abierto,
            utilizando los 8 procesos mas comunes del enfoque DevOps y apoyandose del estandar IEEE 2675 for DevOps
        """
                        )
                    ],
                    className="home",
                ),
                html.Img(src=app.get_asset_url("devops.png")),
            ]
        )
    if pathname == "/plan":
        # return html.Div([dbc.Row(dbc.Col(html.Div("Proceso de Planificacion. En esta fase se definen los requisitos y valores empresariales. Indicador:Puntos de historia"))),]),html.Div(planLayout)
        return "/", html.Div(planLayout)
    if pathname == "/cod":
        return html.Div(codLayout)
    # return  html.P("Proceso de Codificacion. Esta fase implica el diseño del software y la creacion del codigo. Indicador:Tasa de defectos"),codLayout
    if pathname == "/cons":
        return consLayout, html.P(
            "Proceso Construccion o Compilacion. En esta fase se gestionan las versiones y las compilaciones del software"
            "se utilizan herramientas automatizadas que ayudan a compilar y crear paquetes de codigo para publicarlos posteriormente en un ambiente de produccion.Indicador:Tasa de defectos "
        )
    if pathname == "/pru":
        return pruLayout, html.P(
            "Proceso de Pruebas. En esta fase se realizan pruebas unitarias, de integracion y pruebas funcionales para validar la calidad del software y asegurar que cumpla con los requisitos definidos. Indicador:Tasa de defectos "
        )
    if pathname == "/lan":
        return lanLayout, html.P(
            "Proceso de Lanzamiento. En esta fase se lleva a cabo la implementacion del software en el ambiente de produccion, y se realiza el monitoreo de su desempeno. Indicador: Tiempo de despliegue"
        )
    if pathname == "/dsp":
        return dspLayout, html.P(
            "Proceso de Despliegue. En esta fase se lleva a cabo la distribucion del software en diferentes ambientes y se realizan pruebas de aceptacion y evaluacion de su desempeno. Indicador:Tiempo de ciclo de vida"
        )
    if pathname == "/ope":
        return opLayout, html.P(
            "Proceso de Operacion. En esta fase se realiza el monitoreo y mantenimiento del software, se detectan y solucionan errores y se garantiza su disponibilidad y escalabilidad. Indicador:Uptime"
        )
    if pathname == "/mon":
        return monLayout, html.P(
            "Proceso de Monitoreo. En esta fase se lleva a cabo la recoleccion de informacion sobre el desempeno y la disponibilidad del software y se generan alertas ante situaciones anomalias. Indicador: SLA"
        )


# Call app server
if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(debug=True)
