import requests
import matplotlib.pyplot as plt
import url


# Collects Data
def req_data(country):
    request_url = url.url + 'total/country/' + country
    info = requests.get(request_url)
    data = info.json()
    confirmed(data, country)
    death(data, country)
    recovered(data, country)


def graph(x, y, name, country):
    plt.plot(x, y)
    plt.xlabel('Time')
    plt.ylabel(f'No.of {name}')
    try:
        plt.title(f'{country}')
    except:
        pass
    plt.show()


def confirmed(cases, country):
    x = []
    y = []
    flag = 0
    for case in cases:
        if(flag == 0):
            if(case['Date'][:10]!='2020-03-01'):
                continue
            else:
                flag = 1
        x.append(case['Date'][:10])
        y.append(case['Confirmed'])
    graph(x, y, "Confirmed Cases", country)


def death(cases, country):
    x = []
    y = []
    flag = 0
    for case in cases:
        if (flag == 0):
            if (case['Date'][:10] != '2020-03-01'):
                continue
            else:
                flag = 1
        x.append(case['Date'][:10])
        y.append(case['Deaths'])
    graph(x, y, "Death Cases", country)


def recovered(cases, country):
    x = []
    y = []
    flag = 0
    for case in cases:
        if (flag == 0):
            if (case['Date'][:10] != '2020-03-01'):
                continue
            else:
                flag = 1
        x.append(case['Date'][:10])
        y.append(case['Recovered'])
    graph(x, y, "Recovered Cases", country)


if __name__ == "__main__":
    # Collects Query from User
    print("Country Specific Data....................")
    country = input("Enter the Country: ").strip()
    req_data(country)
