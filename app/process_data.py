import requests
from datetime import datetime
import json

def process_data():
    payload={}
    headers={}
    
    date = datetime.today().strftime('%Y-%m-%d')
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{ date }/currencies/gbp.json"
    
    response = requests.request("GET", url, headers=headers, data=payload)
    json_ver = json.loads(response.text)
    # Tracking JPY Yen and putting it in Influx
    japan_yen = json_ver["gbp"]["jpy"]
    return japan_yen
    
    
"""if __name__ == '__main__':
    process_data()
"""