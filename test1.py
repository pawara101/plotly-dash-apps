# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
# app.layout = html.Div([
#     html.Div(children='My First App with Data'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10)
# ])


# App layout
app.layout = html.Div([
    html.Div(children='Dash App'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=15),
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')),
    dcc.Graph(figure=px.line(df, x='country', y='gdpPercap')),
    dcc.Graph(figure=px.histogram(df, x='continent', y='gdpPercap', histfunc='avg'))
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
