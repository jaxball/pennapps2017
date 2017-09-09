import requests
import json

url = 'https://data.chastiser11.hasura-app.io/v1/query'

symbol = "GOOGL"
market = "NASDAQ"
numDays = "3"
predictions = [234, 450, 390] 

payload = {"type": "insert", "args":{"table": "stockforecast", "objects": [{"stocksymbol": symbol, "market": market, "period": numDays, "predictions": results }]}}
headers = {"content-type": "application/json", "authorization": "Bearer wj7fmf21w6lvu0l4u7vmdef1tqo0cykn"}
r = requests.post(url, json.dumps(payload), headers=headers)
if r.status_code == 200:
    print 'success'   
else:
    return 'error: ' + str(r.status_code) + '\n\n' + r.text