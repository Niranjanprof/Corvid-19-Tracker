import jsontodict as info

# Collects Data
data = info.data['locations']

# Collects Query from User
country = input("Enter the Country: ")
province = input("Enter the Province: ")

# For Countries with Province same as the Country
if country == province:
    province = ''


coordinates = {}
confirmed = None
deaths = None
recovered = None
last_updated = None

for datum in data:
    if country == datum['country']:
        if province.strip() == datum['province'].strip():
            last_updated = datum['last_updated'][:10]
            coordinates['latitude'] = datum['coordinates']['latitude']
            coordinates['longitude'] = datum['coordinates']['longitude']
            confirmed = datum['latest']['confirmed']
            deaths = datum['latest']['deaths']
            recovered = datum['latest']['recovered']
            break

# As a part of Formatting
if province.strip() == '':
    province = country



print('\n\n\n')
print('Country: {} Province: {} \n ...........As on last update: {}'.format(country, province, last_updated))
print('\n\n\n')
print('Co-coordinates........')
print(f"Latitude: {coordinates['latitude']}")
print(f"Longitude: {coordinates['longitude']}")
print('\n\n\n')
print("Cases:     ")
print(f'Confirmed Cases: {confirmed}')
print(f'No. of Deaths: {deaths}')
print(f'Recovered Cases: {recovered}')