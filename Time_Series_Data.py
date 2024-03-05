import requests
import json
import pandas as pd
from datetime import datetime

url = 'https://api.cognitedata.com/api/v1/projects/publicdata/timeseries/data/list'
myobj = {
   "items":[
             {
                    "id": 643849686863640

                }
    ],
    "start": 1546300800000,
    "end": 1575158400000,
    "granularity": "1d",
    "aggregates": [
                    "average"
      ]
}

# print(f"TS Start Time {datetime.fromtimestamp(myobj["start"]/ 1000)}")

start_time = datetime.fromtimestamp(myobj["start"]/ 1000)
end_time = datetime.fromtimestamp(myobj["end"]/ 1000)
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSIsImtpZCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSJ9.eyJhdWQiOiJodHRwczovL2FwaS5jb2duaXRlZGF0YS5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80OGQ1MDQzYy1jZjcwLTRjNDktODgxYy1jNjM4ZjU3OTY5OTcvIiwiaWF0IjoxNzA5Mjk5NzM1LCJuYmYiOjE3MDkyOTk3MzUsImV4cCI6MTcwOTMwNDM4MywiYWNyIjoiMSIsImFpbyI6IkFZUUFlLzhXQUFBQUtvK3J4NGwwRjUvM3IyMzFXdUU4WWhNd2xPUHVtVEpCanVTbGFjMWJMbkdYNzVCWE15SnRiVXJJOCs5N3hFVXZaWk93cFYvTmVKRnJYWG5lWmVZSjA2aTZzR2tVOFlVQ0hTTk5YTGxscmV3VnVXeFZKODNXMHQ3R1ljMi9qcGRLaW9HTE1meDhLNVRlRWROc0U1NjY4eHphaG1oeFVVRklyK1o4TVNTbVBRdz0iLCJhbXIiOlsicHdkIl0sImFwcGlkIjoiYTE4MTAwYjItMjhiOC00ZTUxLTkwZmMtNDlmZmQwOTg5YTMxIiwiYXBwaWRhY3IiOiIwIiwiZW1haWwiOiJwYXdhcmExMDFkYXNzYW5heWFrZUBnbWFpbC5jb20iLCJmYW1pbHlfbmFtZSI6IlRoYXJrYW5hIiwiZ2l2ZW5fbmFtZSI6IlBhd2FyYSIsImhhc2dyb3VwcyI6InRydWUiLCJpZHAiOiJsaXZlLmNvbSIsImlwYWRkciI6IjExMi4xMzQuMjE2LjM1IiwibmFtZSI6InBhd2FyYSIsIm9pZCI6ImU4YmNkOTc3LTdhOTUtNGU2Ny1iYjdkLWRjYzdjZTc3MjI0NyIsInJoIjoiMC5BWG9BUEFUVlNIRFBTVXlJSE1ZNDlYbHBsNWEzcTN4bXVfSkt1T1FYcGNQMmlzUjZBRTguIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoibHVpTEJ6QnVoVDRLTzRDMnJYVUVhQS13dHJPS20ybUhDclU2Rmlqb2VaRSIsInRpZCI6IjQ4ZDUwNDNjLWNmNzAtNGM0OS04ODFjLWM2MzhmNTc5Njk5NyIsInVuaXF1ZV9uYW1lIjoibGl2ZS5jb20jcGF3YXJhMTAxZGFzc2FuYXlha2VAZ21haWwuY29tIiwidXRpIjoiYVlNN2R5U2pTMHV5NWh0M1lodHJBUSIsInZlciI6IjEuMCJ9.UG4Yv1XWqlXD5t7ukEjdNSz3SXMWxPMTBeBLRX-V9usS6YH8mEmXGvYC8v0IE61yPrG41wd9C07I9X8WiP8ORkdUfhi7aybN_hebYV4ztm-RF__tzJ2EPcsjZRF_sdtP9rs90cBOSNv_KCJDfADF2i0y-lwpFSJ7oz_bJWFtx1tIgWGVX_fmT9IlbcOke-iFBJrQewBSNwfogWcXmCZOCm29B7pqlBOVvst3zEiUfJolm3r6JcxRw9_q7PmECVSm4kBtuQ3daphSPc1tVxIUnKChNkCwxESd1_gB5n-XtjS00iq5kg9yd1P3VZMaoc32xMffWcqspmcfHjkysJbyVA',
    'Content-Type': 'application/json',
}

x = requests.post(url, json=myobj, headers=headers)
TS_data = x.json()

print(TS_data)

print('--------------------------------')
# print(TS_data['items'][0]['datapoints'])

data_dict = TS_data['items'][0]['datapoints']

df = pd.DataFrame.from_dict(data_dict, orient='columns')  # 'columns' ensures column-wise orientation
df['timestamp'] = pd.to_datetime(df['timestamp'],unit='ms')
df['timestamp'] = df['timestamp'].dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
print(df.head())

## Ploty Dashboard
from dash import Dash, html, dcc, callback, Output, Input , dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

BS = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
app = Dash(__name__, external_stylesheets=[BS])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(children=f'Time Series data of {TS_data['items'][0]["externalId"]} from {start_time} to {end_time}'),
            dcc.Graph(figure=px.line(df['average'],df['timestamp'])),
            dash_table.DataTable(data=df.to_dict('records'), page_size=20)

        ]),
    ]),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)