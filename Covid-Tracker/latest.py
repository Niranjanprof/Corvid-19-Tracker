import jsontodict as info

# Collects data from api
confirmed = info.data['latest']['confirmed']
deaths = info.data['latest']['deaths']
recovered = info.data['latest']['recovered']
last_updated = info.data['locations'][0]['last_updated'][:10]

# Prints Global Data
print("Cases:     ")
print(f'As on Last Update: {last_updated}')
print(f'Confirmed Cases: {confirmed}')
print(f'No. of Deaths: {deaths}')
print(f'Recovered Cases: {recovered}')