from dash import Dash, html, dash_table, dcc, callback, Output, Input



app = Dash(__name__)

app.layout =  html.Div([
html.H1("Hello"),

dcc.Checklist(
    ['New York City', 'Montréal', 'San Francisco'],
    ['New York City', 'Montréal'],
    inline=True
)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)