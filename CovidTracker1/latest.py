import jsontodict as info
import matplotlib.pyplot as plt
# Collects data from api
confirmed = info.data['latest']['confirmed']
deaths = info.data['latest']['deaths']
last_updated = info.data['locations'][0]['last_updated'][:10]

# Prints Global Data
print("Cases:     ")
print(f'As on Last Update: {last_updated}')
print(f'Confirmed Cases: {confirmed}')
print(f'No. of Deaths: {deaths}')

slices=[confirmed,deaths]

activities=['Confirmed Cases','No. of Deaths']
color=['b','r']
plt.pie(slices,labels=activities,colors=color,startangle=90,shadow=True,explode=(0,0.2),autopct='%1.2f%%')
plt.title("Global")
plt.legend(loc='best', bbox_to_anchor=(0.8, 0, 0.3, 0.2))
plt.show()
