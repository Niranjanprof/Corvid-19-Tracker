import requests

try:
    # Collects Data from the api
    response = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations?timelines=true')
except:
    print('Network Error: Check your Connection')
    exit()
# Converts to python dictionary
data = response.json()