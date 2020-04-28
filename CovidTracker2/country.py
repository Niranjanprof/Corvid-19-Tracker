import requests
import timeline
import matplotlib.pyplot as plt
import url

# Collects Query from User
print("Country Specific Data....................")
country = input("Enter the Country: ").strip()

# Collects Data
request_url = url.url + 'total/country/' + country
info = requests.get(request_url)
data = info.json()[-1]

coordinates = dict(lat=data['Lat'], lon=data['Lon'])
confirmed = data['Confirmed']
deaths = data['Deaths']
recovered = data['Recovered']
country_code = data['CountryCode']
last_updated = data['Date'][:10]

print('\n\n\n')
print('Country: {} as on last update: {}'.format(country, last_updated))
print('\n')
print('Co-coordinates........')
print(f"Latitude: {coordinates['lat']}")
print(f"Longitude: {coordinates['lon']}")
print('\n\n\n')
print("Cases:     ")
print(f'Confirmed Cases: {confirmed}')
print(f'No. of Deaths: {deaths}')
print(f'Recovered Cases: {recovered}')

slices=[confirmed,deaths,recovered]

activities=['Confirmed Cases','No. of Deaths','Recovered Cases']
color=['g','r','tab:orange']
plt.pie(slices,labels=activities,colors=color,startangle=90,shadow=True,explode=(0,0,0.2),autopct='%1.2f%%')
plt.title(country)
plt.legend(loc='best', bbox_to_anchor=(0.8, 0, 0.3, 0.2))
plt.show()

timeline.req_data(country)

