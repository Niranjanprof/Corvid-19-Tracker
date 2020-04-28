import requests
import time

while True: 
    try:
        # Collects Data from the api
        response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations?timelines=true')
    except:
        print("Network down.")
        time.sleep(1)
    else:
        break
# Converts to python dictionary
data = response.json()