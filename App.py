import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv("Communaute.csv")
#df = df.groupby('Statut')[['Street_robbery', 'Drugs']].median()
df = df.groupby('Statut')


app.layout = html.Div([
        dbc.Row(dbc.Col(html.H3("Dashboard datacraft"),
                        width={'size': 2 , 'offset': 5},
                        ),
                ),
    
                
        dbc.Row(
            [
                dbc.Col(dbc.Button(children="Vive", size = 4, color="primary", className="me-1",
                        style={'font-size': '50px', 'width': '100%', 'display': 'inline-block', 'height':'800px'}),
                        ),
                
    
                dbc.Col(dbc.Button("la", size = 4, color="light", className="me-2",
                        style={'font-size': '50px', 'width': '100%', 'display': 'inline-block', 'height':'800px'}),
                        ),
                
                dbc.Col(dbc.Button("France", color="danger", className="me-3",
                        style={'font-size': '50px', 'width': '100%', 'display': 'inline-block', 'height':'800px'}),
                        ),
                ]),
        
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(id='a_dropdown', placeholder='Type de personne',
                                     options=[{'label': 'Freelance en résidence', 'value': 'freelance'},
                                              {'label': 'Full membership', 'value': 'full'},
                                              {'label': 'Corporate membership', 'value': 'corporate'},
                                              {'label': 'Chercheur en résidence', 'value': 'chercheur'}]),
                        width={'size': 4, "offset": 4, 'order':1 }),
            ]),
])


if __name__ == '__main__':
    app.run_server(debug=True)


#@app.callback(
#    [Output('pie_chart1', 'figure'),
#     Output('pie_chart2', 'figure')],
#    [Input('a_dropdown', 'value'),
#     Input('b_dropdown', 'value')]
#)
