from bs4 import BeautifulSoup
import requests
import time


def convert(number):
    accum = 0
    numbers = number.split(',')
    for i in numbers:
        accum = accum * 100 + int(i)
    return accum

file= open('population.txt','w')
maper = open('map.txt')
while True:
    for line in maper:
        country = line.strip()
        try:
            flag = resource[:2]
        except:
            try:
                url = r'https://www.worldometers.info/world-population/population-by-country/'
                resource = requests.get(url).text
            except:
                print("Bad Connection")
                continue
        else:
            if time.localtime()[4] == 0 and time.localtime()[5] == 0:
                try:
                    url = r'https://www.worldometers.info/world-population/population-by-country/'
                    resource = requests.get(url).text
                except:
                    print("Bad Connection")
                    continue
        souped_resource = BeautifulSoup(resource, "html.parser")
        all_tr = souped_resource.find_all('tr')
        flag = 0
        count = 0
        data = None
        for tr in all_tr:
            all_td = tr.find_all('td')
            for td in all_td:
                if flag == 1:
                    data = td.string
                    count += 1
                    if count > 0:
                        break
                try:
                    if td.string.startswith(country):
                        flag = 1
                except:
                    continue
            if count > 0:
                break

        try:
            print("Total Population: " + data)
            file.write(country+' '+data+'\n')

        # plt.pie([convert(data[0]), convert(data[2]), convert(data[4])],
        #       labels=['Confirmed Cases', 'No. of Deaths', 'Recoverd Cases'], colors=['tab:orange', 'r', 'g'],
        #       startangle=45, shadow=True, explode=(0, 0, 0.2), autopct='%1.2f%%')
        # plt.title("World-Wide")
        # plt.legend(loc='best', bbox_to_anchor=(0.8, 0, 0.3, 0.2))
        # plt.show()

        except:
            print("Wrong Input")
            file.write(country + ' ' + "Wrong\n")
            quit()

