import os

import requests
from dotenv import load_dotenv


def get_trains(crs, destination_name) :
    load_dotenv()

    api_key = os.getenv('RAILDATA_API_KEY')

    # crs = 'WOK'

    url = f'https://api1.raildata.org.uk/1010-live-arrival-board-arr/LDBWS/api/20220120/GetArrBoardWithDetails/{crs}'

    headers = {
        'User-Agent' : "",
        'x-apikey' : api_key
    }
    # print("RailData API key loaded:", bool(api_key))

    response = requests.get(url, headers=headers)

    # print('status code :', response.status_code)
    # print(response.text[:1000])

    data = response.json()
    # print(type(data))
    # print(data.keys())

    train_services = data['trainServices']
    # print(type(train_services))
    # print(len(train_services))
    results = []
    for train in train_services:
        destination_ = train['destination']
        destination = destination_[0]['locationName']
        scheduled = train.get('sta', 'Unknown')
        estimated = train.get('eta', 'Unknown')
        platform = train.get('platform', 'Unknown')
        cancelled = train.get('isCancelled', 'Unknown')

        if destination == destination_name :
            results.append({
                'destination' : destination,
                'scheduled' : scheduled,
                'estimated' : estimated,
                'platform' : platform,
                'cancelled' : cancelled
            }) 

    return results

# trains = get_trains('WOK', "London Waterloo")
# print(trains)

