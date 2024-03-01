import requests
import json

url = 'https://api.cognitedata.com/api/v1/projects/publicdata/timeseries/data/list'
myobj = {
   "items":[
             {
                    "id": 643849686863640

                }
    ],
    "start": 1548979200000,
    "end": 1551398399000,
    "granularity": "1d",
    "aggregates": [
                    "average"
      ]
}

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSIsImtpZCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSJ9.eyJhdWQiOiJodHRwczovL2FwaS5jb2duaXRlZGF0YS5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80OGQ1MDQzYy1jZjcwLTRjNDktODgxYy1jNjM4ZjU3OTY5OTcvIiwiaWF0IjoxNzA5Mjk1MDI1LCJuYmYiOjE3MDkyOTUwMjUsImV4cCI6MTcwOTI5OTc0OCwiYWNyIjoiMSIsImFpbyI6IkFZUUFlLzhXQUFBQXdOV2g1clBzWDViZktsdExJcUR1MWo0TW4xdDBzS1IxMlJCRmJlMFB1Rk5iZ2JGdHN6QWovcGRibG1pUW1nL2VKNTB5TkhwWWRpMUNVU1p1UU90d3V1ZE1EQjB6SWlBd1FSTzFLK3gvREppODZnN1g0cHpCbHh3bzMrU1NyRHdVaVZHU3hKT2xFYUZ0c2dLSm8wVWs2dzBISnNkT3FIbVJPRXgvd0V4cUtpOD0iLCJhbXIiOlsicHdkIl0sImFwcGlkIjoiYTE4MTAwYjItMjhiOC00ZTUxLTkwZmMtNDlmZmQwOTg5YTMxIiwiYXBwaWRhY3IiOiIwIiwiZW1haWwiOiJwYXdhcmExMDFkYXNzYW5heWFrZUBnbWFpbC5jb20iLCJmYW1pbHlfbmFtZSI6IlRoYXJrYW5hIiwiZ2l2ZW5fbmFtZSI6IlBhd2FyYSIsImhhc2dyb3VwcyI6InRydWUiLCJpZHAiOiJsaXZlLmNvbSIsImlwYWRkciI6IjExMi4xMzQuMjE2LjM1IiwibmFtZSI6InBhd2FyYSIsIm9pZCI6ImU4YmNkOTc3LTdhOTUtNGU2Ny1iYjdkLWRjYzdjZTc3MjI0NyIsInJoIjoiMC5BWG9BUEFUVlNIRFBTVXlJSE1ZNDlYbHBsNWEzcTN4bXVfSkt1T1FYcGNQMmlzUjZBRTguIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoibHVpTEJ6QnVoVDRLTzRDMnJYVUVhQS13dHJPS20ybUhDclU2Rmlqb2VaRSIsInRpZCI6IjQ4ZDUwNDNjLWNmNzAtNGM0OS04ODFjLWM2MzhmNTc5Njk5NyIsInVuaXF1ZV9uYW1lIjoibGl2ZS5jb20jcGF3YXJhMTAxZGFzc2FuYXlha2VAZ21haWwuY29tIiwidXRpIjoiYUpHZHY4S2FtRVdtTU40dE5QUU1BUSIsInZlciI6IjEuMCJ9.TsJDQ7A8IuRCY9M0rsq8lyUYiiD_1SS4HvOw6sgFzZpE6_vFT8a1moDRFC2wPoVjru4H3zt-VYaNwAmViMtDMzZ-8E992OwmYiDvT3-oDzOF0duYQdsn1RSK-L6af0ZZqkjSFD48cMB4pRL8MfnA_7L0VOVinEjFWPYJhyWLWO_fvS1cFf6wpLTYSVZww8ZhtuHcWY5zI_NzeaWObzn-B9jcIthB6lXx3D5PT6U90aAeeJd4M37gYvaNFTcquGTRMAHJKnjNYjOiLg0VKxzd8pL0Ei5vKzv7FHXM9kg_ztly1IhxtqTdJ5mPlzQqarUIEfXWkgevh7jGykiz38EVrA',
    'Content-Type': 'application/json',
}

x = requests.post(url, json=myobj, headers=headers)
TS_data = x.json()

print(TS_data)
