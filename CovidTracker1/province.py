import jsontodict as info
import matplotlib.pyplot as plt
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


slices=[confirmed,deaths]

activities=['Confirmed Cases','No. of Deaths']
color=['b','r']
plt.pie(slices,labels=activities,colors=color,startangle=0,shadow=True,explode=(0,0.2),autopct='%1.2f%%')
plt.title(country+"\n"+province)
plt.legend(loc='best', bbox_to_anchor=(0.8, 0, 0.3, 0.2))
plt.show()
