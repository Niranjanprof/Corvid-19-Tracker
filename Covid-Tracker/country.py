import jsontodict as info

# Collects Data
data = info.data['locations']

# Collects Query from User
print("Country Specific Data....................")
country = input("Enter the Country: ")

coordinates = {}
confirmed = []
deaths = []
recovered = []
flag = 0
country_code = None
country_population = None
country_province = []
last_updated = None

for datum in data:
    if flag == 1:
        if country != datum['country']:
            break
            # to break when country repetition is over

    if country == datum['country']:
        country_population = datum['country_population']
        last_updated = datum['last_updated'][:10]
        coordinates['latitude']= datum['coordinates']['latitude']
        coordinates['longitude'] = datum['coordinates']['longitude']
        confirmed.append(datum['latest']['confirmed'])
        deaths.append(datum['latest']['deaths'])
        recovered.append(datum['latest']['recovered'])
        flag = 1
        # to sum up country repetition


print('\n\n\n')
print('Country: {} as on last update: {}'.format(country,last_updated))
print('\n')
print(f'Population: {country_population}')
print('\n\n\n')
print('Co-coordinates........')
print(f"Latitude: {coordinates['latitude']}")
print(f"Longitude: {coordinates['longitude']}")
print('\n\n\n')
print("Cases:     ")
print(f'Confirmed Cases: {sum(confirmed)}')
print(f'No. of Deaths: {sum(deaths)}')
print(f'Recovered Cases: {sum(recovered)}')