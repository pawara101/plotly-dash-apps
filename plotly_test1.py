import numpy as np # linear algebra
import pandas as pd 

from dash import Dash, html, dcc, callback, Output, Input , dash_table
import plotly.graph_objs as go

import plotly.express as px

timesData = pd.read_csv("https://raw.githubusercontent.com/arnaudbenard/university-ranking/master/timesData.csv")

df = timesData.iloc[:100,:]

trace1 = go.Scatter(
                    x = df.world_rank,
                    y = df.citations,
                    mode = "lines",
                    name = "citations",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text= df.university_name)

trace2 = go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = "lines+markers",
                    name = "teaching",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                    text= df.university_name)


layout = dict(title = 'Citation and Teaching vs World Rank of Top 100 Universities',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False)
             )

df2016 = timesData[timesData.year == 2016].iloc[:7,:]
pie1 = df2016.num_students

pie1_list = [float(each.replace(',', '.')) for each in df2016.num_students]  # str(2,4) => str(2.4) = > float(2.4) = 2.4
labels = df2016.university_name

## Dash App
app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='World University Ranking Statistics'),
    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x = df.world_rank,
                    y = df.citations,
                    mode = "lines",
                    name = "citations",
                    
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text= df.university_name),
                go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = "lines+markers",
                    name = "teaching",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                    text= df.university_name)
            ],
            layout=go.Layout(
                title = 'Citation and Teaching vs World Rank of Top 100 Universities',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False)
            )
        )
    ),
    ## Pie Chart
    dcc.Graph(
        figure = px.pie(df2016, values=pie1, names=labels, hole=.3)
    )
    
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
