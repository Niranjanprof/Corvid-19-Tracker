import requests
import matplotlib.pyplot as plt


def graph(x, y, z, country):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x, y, label='No. of Deaths')
    ax.plot(x, z, label='Confirmed Cases')

    plt.xlabel('Time')
    plt.xticks(rotation=90)
    try:
        plt.title(f'{country}')
    except:
        pass
    plt.legend(loc=2)
    plt.show()


country = input("Enter your Country: ").strip()
if country.strip() == '':
    print("Invalid Name")
    quit()
url = None
with open('countryurl.txt') as file:
    for line in file:
        if line.startswith(country):
            url = line.strip().split()[-1]
if url is None:
    print("Invalid Name")
    quit()
try:
    info = requests.get('https://www.worldometers.info/coronavirus/' + url).text
except:
    print("BAD Connection")
flag = 0
lines = info.split('\n')
for line in lines:
    if flag == 1:
        if line.strip().startswith('categories: ['):
            dates = line.split(',')
            break
    if line.strip().startswith("text: 'Total Coronavirus Cases'"):
        flag = 1
dates[0] = dates[0].strip()[13:]
del (dates[-1])
dates[-1] = dates[-1][:8]
new_dates = []
for date in dates:
    new_date = ''
    for c in date:
        if c.isalnum():
            new_date += c
    new_dates.append(new_date)

print(new_dates)

flag = 0
for line in lines:
    if flag == 1:
        if line.strip().startswith("data:"):
            confirmed_y = line.split(',')
            break
    if line.strip().startswith("text: 'Total Coronavirus Cases'"):
        flag = 1
confirmed_y[0] = confirmed_y[0].strip()[7:]
del (confirmed_y[-1])

new_y = []
for value in confirmed_y:
    new_value = ''
    for c in value:
        if c.isalnum():
            new_value += c
    new_y.append(new_value)

confirmed_y = [int(x) for x in new_y]
print(confirmed_y)

flag = 0
for line in lines:
    if flag == 1:
        if line.strip().startswith("data:"):
            death_y = line.split(',')
            break
    if line.strip().startswith("text: 'Total Coronavirus Deaths'"):
        flag = 1
death_y[0] = death_y[0].strip()[7:]
del (death_y[-1])

new_death_y = []
for value in death_y:
    new_value = ''
    for c in value:
        if c.isalnum():
            new_value += c
    new_death_y.append(new_value)

death_y = [int(x) for x in new_death_y]
print(death_y)

graph(new_dates, confirmed_y, death_y, country)
