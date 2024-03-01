from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

external_stylesheets = [dbc.themes.CYBORG]
BS = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
app = Dash(__name__, external_stylesheets=[BS])

# app.layout = html.Div([
#     html.H1(children='World Stats', style={'textAlign':'center'}),
#     dcc.Dropdown(options=[{'label': country, 'value': country} for country in df['country'].unique()],
#                  value='Canada', id='dropdown-selection'),
#     dcc.Dropdown(options=[{'label': cat, 'value': cat} for cat in ['pop', 'lifeExp', 'gdpPercap']],
#                  id='dropdown-selection-cat', value='pop'),
#     dcc.Graph(id='graph-content')
# ])


# Define a dark theme using CSS
dark_theme = '''
    body {
        background-color: #2a2a2a;
        color: #ffffff;
    }
    .dropdown-item {
        color: #ffffff !important;
    }
    .form-label {
        color: #ffffff !important;
    }
    .fs-3 {
        color: #17a2b8 !important;
    }
    .btn-primary {
        background-color: #17a2b8 !important;
        border-color: #17a2b8 !important;
    }
    .btn-primary:hover {
        background-color: #117a8b !important;
        border-color: #117a8b !important;
    }
'''




app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(children='World Stats', className="text-primary text-center fs-3"),
            dbc.Label("Country"),
            dcc.Dropdown(options=[{'label': country, 'value': country} for country in df['country'].unique()],
                         value='Canada', id='dropdown-selection'),
                         dbc.Label("Parameter"),
            dcc.Dropdown(options=[{'label': cat, 'value': cat} for cat in ['pop', 'lifeExp', 'gdpPercap']],
                         id='dropdown-selection-cat', value='pop'),
            dcc.Graph(id='graph-content')
        ]),
    ]),
], style={'stylesheet': dark_theme})

@app.callback(
    Output('graph-content', 'figure'),
    [Input('dropdown-selection', 'value'), 
     Input('dropdown-selection-cat', 'value')
     ]
)
def update_graph(value, cat):
    dff = df[df['country'] == value]
    return px.line(dff, x='year', y=cat)

if __name__ == '__main__':
    app.run(debug=True)
