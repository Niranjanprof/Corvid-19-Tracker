import requests
import url

request_url = url.url + 'world/total'

info = requests.get(request_url)
data = info.json()


confirmed = data['TotalConfirmed']
deaths = data['TotalDeaths']
recovered = data['TotalRecovered']

# Prints Global Data
print("Cases:     ")
print(f'Confirmed Cases: {confirmed}')
print(f'No. of Deaths: {deaths}')
print(f'Recovered Cases: {recovered}')