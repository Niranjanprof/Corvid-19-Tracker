import requests

info = requests.get('https://coronavirus-tracker-api.herokuapp.com/v2/locations')

data = info.json()['locations']
js = {}
country = ''
with open('data.txt','w') as file:
    for datum in data:
        if(country == datum['country']):
            continue
        country = datum['country']
        js[country] = datum['country_code'] + ' ' + str(datum['country_population']) + ' ' + datum['coordinates']['latitude'] +' '+ datum['coordinates']['longitude']
    order ={}
    for key in sorted(js.keys()):
        order[key] = js[key]
    print(order)
    for key in order:
        file.write(key+' '+order[key]+'\n')



