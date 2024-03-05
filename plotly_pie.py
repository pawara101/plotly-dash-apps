from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)
df = px.data.tips() # replace with your own data source

app.layout = html.Div([
    html.H4('Analysis of the restaurant sales'),
    dcc.Graph(id="graph",figure=px.pie(df, values="total_bill", names="smoker", hole=.3)),
])


# @app.callback(
#     Output("graph", "figure"), 
#     Input("names", "value"), 
#     Input("values", "value"))
# def generate_chart(names, values):
#     df = px.data.tips() # replace with your own data source
#     fig = px.pie(df, values=values, names=names, hole=.3)
#     return fig


app.run_server(debug=True)