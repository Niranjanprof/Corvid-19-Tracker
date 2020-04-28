import requests
import timeline

import url

# Collects Query from User
print("Country Specific Data....................")
country = input("Enter the Country: ").strip()

# Collects Data
request_url = url.url + 'live/country/'+country
info = requests.get(request_url)
data = info.json()[-1]

coordinates = dict(lat = data['Lat'],lon = data['Lon'])
confirmed = data['Confirmed']
deaths = data['Deaths']
recovered = data['Recovered']
active = data['Active']
country_code = data['CountryCode']
last_updated = data['Date'][:10]


print('\n\n\n')
print('Country: {} as on last update: {}'.format(country,last_updated))
print('\n')
print('Co-coordinates........')
print(f"Latitude: {coordinates['lat']}")
print(f"Longitude: {coordinates['lon']}")
print('\n\n\n')
print("Cases:     ")
print(f'Confirmed Cases: {confirmed}')
print(f'No. of Deaths: {deaths}')
print(f'Recovered Cases: {recovered}')
timeline.req_data(country)