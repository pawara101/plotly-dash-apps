from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='drop-down-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content','figure'),
    Input('drop-down-selection','value')
)
def update_graph(value):
    df_set = df[df.country == value]
    return px.line(df_set,x='year',y='pop')

if __name__ == '__main__':
    app.run(debug=True)


