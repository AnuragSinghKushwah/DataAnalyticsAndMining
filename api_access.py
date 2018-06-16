import pandas as pd
import requests
import json

def read_data_api(ticker_name, start_date, end_date, freq_in_min):
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Token 243605654ef881d04ecd512109c9244d54486a9d'}
    # get_url = "https://api.tiingo.com/iex/VMW/prices?startDate=2017-05-01&endDate=2017-05-1&resampleFreq=1min"
    get_url = "https://api.tiingo.com/iex/"+ticker_name+"/prices?startDate="+start_date+"&endDate="+end_date+"&resampleFreq="+str(freq_in_min)
    requestResponse = requests.get(get_url, headers=headers)
    # print("requestResponse : ",requestResponse)
    df = pd.DataFrame(requestResponse.json())
    print("response dataframe : ",df.head())

    # Saving data to csv file
    df.to_csv("full_year_ndaq_data.csv")

    # records = json.loads(df.T.to_json()).values()
    # # Saving Data to mongodb
    # for event in records:
    #     print("event : ",event)
    #     event["ticker"] = ticker_name
    #     event["frequency"] = freq_in_min
    #     event["flag"] = "5year"
    #     # inserting
    #     db.insert(event)
    # return df

# read_data_api('TSLA','2017-05-01','2017-05-01',freq_in_min='1min')

import requests
from pprint import pprint
headers = {
    'Content-Type': 'application/json'
}
# get = requests.get(url="https://reqres.in/api/users?page=2")

body = {"email": "sydney@fife","password": "pistol"}

# get = requests.get(url="https://reqres.in/api/users?page=2")

post = requests.post(url="https://reqres.in/api/register",json=body)
pprint(post.json())
# for i in get.json()['data']:
#     print(i['first_name'])

# sample_data = {'data':{'summary':'an introduction to python',"intro":'whatever you want'},
#                ""}






