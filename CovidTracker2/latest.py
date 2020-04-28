import requests
import url
import matplotlib.pyplot as plt

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


slices=[confirmed,deaths,recovered]

activities=['Confirmed Cases','No. of Deaths','Recovered Cases']
color=['g','r','tab:orange']
plt.pie(slices,labels=activities,colors=color,startangle=90,shadow=True,explode=(0,0,0.2),autopct='%1.2f%%')
plt.title("Global")
plt.legend(loc='best', bbox_to_anchor=(0.8, 0, 0.3, 0.2))
plt.show()
