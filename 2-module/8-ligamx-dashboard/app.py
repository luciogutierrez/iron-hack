import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import numpy as np

data = pd.read_csv("liga-mx-c-2021.csv")
indicadores = {'pts_a':'Puntos','gf_a':'Goles a favor','gc_a':'Goles en Contra','gd_a':'Diferencia de goles',
               'pg_a':'Partidos ganados','pe_a':'Partidos empatados','pp_a':'Partidos perdidos'}

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Liga MX - Torneo Clausura 2021"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src='/assets/equipos.png', className="header-img"),
                html.P(children="⚽", className="header-emoji"),
                html.H1(children="Liga MX Clausura 2021", className="header-title"),
                html.P(children="Análisis frente a frente del torneo clausura 2021", className="header-description")
            ], className="header"
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Equipo 1", className="menu-title"),
                        dcc.Dropdown(
                            id="filtro-equipo1",
                            options=[{"label": equipo, "value": equipo}
                                     for equipo in np.sort(data.equipo.unique())
                            ],
                            value="Cruz Azul",
                            clearable=False,
                            searchable=False,
                            className="dropdown"
                        )
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Equipo 2", className="menu-title"),
                        dcc.Dropdown(
                            id="filtro-equipo2",
                            options=[{"label": equipo, "value": equipo}
                                     for equipo in data.equipo.unique()
                            ],
                            value="América",
                            clearable=False,
                            searchable=False,
                            className="dropdown"
                        )
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Indicador", className="menu-title"),
                        dcc.Dropdown(
                            id="filtro-indicador",
                            options=[{"label": indicador, "value": indicador}
                                     for indicador in indicadores.values()
                            ],
                            value="Puntos",
                            clearable=False,
                            searchable=False,
                            className="dropdown"
                        )
                    ]
                )
            ], className="menu"
        ),
        html.Div(
            children=[
                html.Div(children = dcc.Graph(id="grafica-posicion"), className="card")
            ],  className="wrapper"
        )
    ]
)


@app.callback(
    Output("grafica-posicion", "figure"),
    [ Input("filtro-equipo1", "value"), Input("filtro-equipo2", "value"), Input("filtro-indicador", "value")]
)
def update_charts(equipo1, equipo2, indicador):
    dff = data.copy()

    campo = ''.join([key for key, name in indicadores.items() if name == indicador])
    dff['kpi'] = dff[campo]

    dff = dff[(dff.equipo == equipo1) | (dff.equipo == equipo2)]

    fig_posicion = px.line(data_frame=dff, x='jornada', y='kpi', color='equipo', template='plotly_dark')

    return fig_posicion


if __name__ == "__main__":
    app.run_server(debug=True)
