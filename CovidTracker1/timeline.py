import jsontodict as info
import matplotlib.pyplot as plt

data = info.data['locations']

country = input("Enter the country: ")
province = input("Enter the province: ")


def graph(x, y, name):
    plt.plot(x, y)
    plt.xlabel('Time')
    plt.ylabel(f'No.of {name}')
    plt.title(f'{country}')
    plt.show()


def confirmed(cases):
    timeline = cases['timeline']
    x = []
    y = []
    for time in timeline:
        x.append(time[:10])
        y.append(timeline[time])
    graph(x, y, "Confirmed Cases")


def death(cases):
    timeline = cases['timeline']
    x = []
    y = []
    for time in timeline:
        x.append(time[:10])
        y.append(timeline[time])
    graph(x, y, "Death Cases")


for datum in data:
    if country == datum['country']:
        if province.strip() == datum['province'].strip():
            confirmed(datum['timelines']['confirmed'])
            death(datum['timelines']['deaths'])
            break
