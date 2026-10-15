import os
import requests
from dotenv import load_dotenv
from app.train_utils import calculate_delay, get_train_status


def get_trains(crs, destination_name) :
    load_dotenv()

    api_key = os.getenv('RAILDATA_API_KEY')

    # crs = 'WOK'

    url = f'https://api1.raildata.org.uk/1010-live-arrival-board-arr/LDBWS/api/20220120/GetArrBoardWithDetails/{crs}'
    # url =  "https://api1.raildata.org.uk/invalid-test-endpoint"

    headers = {
        'User-Agent' : "",
        'x-apikey' : api_key
    }
    # print("RailData API key loaded:", bool(api_key))
    try:
        response = requests.get(url, headers=headers, timeout = 10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e :
        print('API request failed', e)
        return{"error" : "Failed to retrieve train data"}
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
            delay_minutes = calculate_delay(scheduled, estimated)
            status = get_train_status(scheduled, estimated, cancelled)

            results.append({
                
                'destination' : destination,
                'scheduled' : scheduled,
                'estimated' : estimated,
                'platform' : platform,
                'cancelled' : cancelled,
                'delay_minutes' : delay_minutes,
                'status' : status
            }) 

    return results

if __name__ == "__main__" :
    trains = get_trains('WOK', "London Waterloo")
    print(trains)

