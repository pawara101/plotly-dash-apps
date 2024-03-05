import requests
import json
import pandas as pd
from datetime import datetime

from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthDeviceCode

from dash import Dash, html, dcc, callback, Output, Input , dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

from datetime import datetime, timedelta, timezone

TENANT_ID = "48d5043c-cf70-4c49-881c-c638f5796997"
CLIENT_ID = "1b90ede3-271e-401b-81a0-a4d52bea3273"
BASE_URL = "https://api.cognitedata.com"

oauth_provider = OAuthDeviceCode(
    authority_url=f"https://login.microsoftonline.com/{TENANT_ID}",
    client_id=CLIENT_ID,
    scopes=[f"{BASE_URL}/.default"],
)
client = CogniteClient(
    ClientConfig(
        client_name="Cognite Academy: Intro to PySDK",
        base_url=BASE_URL,
        project="publicdata",
        credentials=oauth_provider,
    )
)

token_info = client.iam.token.inspect()  # 'iam' stands for: Identity and Access Management

print([project.url_name for project in token_info.projects])


# subtree = client.assets.retrieve_subtree(id=4650652196144007)
# print(len(subtree))


# all_timeseries = subtree.time_series()
# print(all_timeseries[1].name)


# TS_data = client.time_series.data.retrieve(external_id="pi:160886", start="10d-ago", end="now", limit=10)
# print((TS_data))

# print(TS_data.id)

train_start_date = datetime(2019,1, 1, tzinfo=timezone.utc)
train_end_date = train_start_date + timedelta(days=90)

ts_exids = ["pi:160697", "pi:160882"]

## Get datapoints directly in a pandas dataframe
datapoints_df = client.time_series.data.retrieve_dataframe(
    external_id=ts_exids,
    aggregates="average",
    granularity="1m",
    start=train_start_date,
    end=train_end_date,
    include_aggregate_name=False,
    uniform_index=True,
)
datapoints_df = datapoints_df.interpolate().dropna()

print(datapoints_df.head())
print(datapoints_df.columns)


print("========================================")
# Ploty Dashboard
BS = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
app = Dash(__name__, external_stylesheets=[BS])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(children=f'Time Series data of {", ".join(ts_exids)}'),
            dcc.Graph(id='graph-col', figure=px.line(datapoints_df[ts_exids[0]])),
            dcc.Graph(id='graph-col', figure=px.line(datapoints_df[ts_exids[1]])),
            dash_table.DataTable(data=datapoints_df.to_dict('records'), page_size=10)

        ]),
    ]),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)