import requests, json
from datetime import date, datetime, timedelta

def rainfall():
    date_today = date.today()
    now = str(datetime.now()-timedelta(hours=1)).replace(' ', 'T')[:-7]

    response = requests.get(
        url = 'https://api.data.gov.sg/v1/environment/air-temperature',
        params = {
            # 'date': date
            'date_time': now
        }
    )
    result = response.json()
    clementi = result['items'][0]['readings'][1]
    temperature = clementi['value']

    response = requests.get(
        url = 'https://api.data.gov.sg/v1/environment/rainfall',
        params={
            'date_time': now
        }
    )

    result = response.json()
    rainfall = result['items'][0]['readings'][5]['value']
    return rainfall

