from bs4 import BeautifulSoup

import requests
import time


while True:
    country = input("Enter a country: ")
    try:
        flag = resource[:2]
    except:
        url = r'https://www.worldometers.info/coronavirus/'
        resource = requests.get(url).text
    else:
        if time.localtime()[4] == 0 and time.localtime()[5] == 0:
            url = r'https://www.worldometers.info/coronavirus/'
            resource = requests.get(url).text
    souped_resource = BeautifulSoup(resource, "html.parser")
    all_tr = souped_resource.find_all('tr')
    flag = 0
    count = 0
    rdata = []
    for tr in all_tr:
        all_td = tr.find_all('td')
        for td in all_td:
            if flag == 1:
                rdata.append(td.string)
                count += 1
                if count > 10:
                    break
            try:
                if td.string.startswith(country):
                    flag = 1
            except:
                continue
        if count > 10:
            break

    print(rdata)
    data = [str(x) for x in rdata]
    print(data)
    try:
        print("Country: " + country)
        print("Total Cases: " + data[0])
        print("New Cases: " + data[1])
        print("Total Deaths: " + data[2])
        print("New Deaths: " + data[3])
        print("Total Recovered: " + data[4])
        print("Active Cases: " + data[5])
        print("Serious,Critical: " + data[6])
        print("Tot Cases/1M pop: " + data[7])
        print("Deaths/1M pop: " + data[8])
        print("TotalTests: " + data[9])
        print("Tests/1M pop: " + data[10])
    except:
        print("Wrong Input")
    i = input("Do you want to run again:(y/n) ")
    if not (i.startswith('y') or i.startswith('Y')):
        break
