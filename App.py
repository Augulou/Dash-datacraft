from dash import Dash, dash_table, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('C:/Users/augus/Documents/Datacraft/V0_Dash/Communaute.csv')
df = df[['fullname','Organisation','Titre','Email','Statut']]

df.fillna("", inplace=True)

app.layout = dbc.Container([
    dcc.Markdown('# Dashboard datacraft', style={'textAlign':'center'}),

    dbc.Label("Nombre de lignes :"),
        row_drop := dcc.Dropdown(value=10, clearable=False, style={'width':'35%'},
                             options=[10, 20, 30]),


    my_table := dash_table.DataTable(
            columns=[
                {'name': 'Nom', 'id': 'fullname', 'type': 'text'},
                {'name': 'Entreprise', 'id': 'Organisation', 'type': 'text'},
                {'name': 'Metier', 'id': 'Titre', 'type': 'text'},
                {'name': 'Mail', 'id': 'Email', 'type': 'text'},
                {'name': 'Statut', 'id': 'Statut', 'type': 'text'}
            ],
            data=df.to_dict('records'),
            filter_action='native',
            page_size=10,
            
            style_data={
            'width': '20%', 'minWidth': '20%', 'maxWidth': '20%',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
                }
            ),
    
        dbc.Row([
            dbc.Col([
                entreprise_drop := dcc.Dropdown([y for y in sorted(df.Organisation.unique())], multi=True)
            ], width=3, style={'margin-left':'35%'}),
            
            dbc.Col([
                statut_drop := dcc.Dropdown([x for x in sorted(df.Statut.unique())], multi=True)
            ], width=3, style={'margin-left':'15%'}),
        ])
])
        
@callback(
    Output(my_table, 'data'),
    Output(my_table, 'page_size'),
    Input(statut_drop, 'value'),
    Input(entreprise_drop, 'value'),
    Input(row_drop, 'value')
)

def update_dropdown_options(statut_v, entreprise_v, row_v):
    dff = df.copy()
    

    if statut_v:
        dff = dff[dff.Statut.isin(statut_v)]
    
    if entreprise_v:
        dff = dff[dff.Organisation.isin(entreprise_v)]

    return dff.to_dict('records'), row_v


if __name__ == '__main__':
    app.run_server(debug=True)
    
    