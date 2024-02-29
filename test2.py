from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(options=[{'label': country, 'value': country} for country in df['country'].unique()],
                 value='Canada', id='dropdown-selection'),
    dcc.Dropdown(options=[{'label': cat, 'value': cat} for cat in ['pop', 'lifeExp', 'gdpPercap']],
                 id='dropdown-selection-cat', value='pop'),
    dcc.Graph(id='graph-content')
])

@app.callback(
    Output('graph-content', 'figure'),
    [Input('dropdown-selection', 'value'), Input('dropdown-selection-cat', 'value')]
)
def update_graph(value, cat):
    dff = df[df['country'] == value]
    return px.line(dff, x='year', y=cat)

if __name__ == '__main__':
    app.run(debug=True)
