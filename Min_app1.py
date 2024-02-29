# Import packages
from dash import Dash, html, dash_table,dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
df_afg = df.loc[df['country'] == "Afghanistan"]
df_can = df.loc[df['country'] == "Canada"]

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='AFG'),
    # dash_table.DataTable(data=df.to_dict(), page_size=10)
    dcc.Graph(figure=px.line(df_afg['year'],df_afg['lifeExp'])),
    html.Div(children='CAN'),
    # dash_table.DataTable(data=df.to_dict(), page_size=10)
    dcc.Graph(figure=px.line(df_can['year'],df_can['lifeExp']))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
