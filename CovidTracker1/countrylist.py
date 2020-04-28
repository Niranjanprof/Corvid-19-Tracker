import jsontodict as info

# Collects Data of Country and Stores it without repetition

data = info.data['locations']
with open('country.txt', 'w') as file:
    country = ''
    for datum in data:
        if country == datum['country']:
            continue
        country = datum['country']
        file.write(country)
        file.write('\n')