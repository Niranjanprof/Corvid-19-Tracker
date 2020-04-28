import requests

import url

# Collects Data
request_url = url.url + 'countries'
info = requests.get(request_url)

data = info.json()

# Collects Data of Country and Stores it without repetition
with open('country.txt', 'w') as file:
    country = ''
    country_list = list()
    for datum in data:
        if country == datum['Country']:
            continue
        country = datum['Country']
        country_list.append(country)
    country_list.sort()
    for country in country_list:
        file.write(country)
        file.write('\n')
