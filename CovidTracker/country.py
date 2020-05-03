import requests
import matplotlib.pyplot as plt

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


def convert(number):
    accum = 0
    numbers = number.split(',')
    for i in numbers:
        accum = accum * 100 + int(i)
    return accum


lines = info.split('\n')
flag = 0
confirmed = ''
recovered = ''
death = ''
for line in lines:
    if flag == 1:
        flag = 0
        words = line.split('>')
        recovered = words[1].split('<')[0]
    if line.startswith('<title>'):
        words = line.split()
        confirmed = words[-7]
        death = words[-4]

    if line.startswith('<div class="maincounter-number" style="color:#8ACA2B ">'):
        flag = 1

print('Confirmed: ' + confirmed)
print('Deaths: ' + death)
print('Recovered:  ' + recovered)
active = convert(confirmed)-convert(death)-convert(recovered)
print('Active: '+str(active))

plt.pie([convert(confirmed), convert(death), convert(recovered)], labels=['Confirmed Cases', 'No. of Deaths', 'Recoverd Cases'], colors=['tab:orange', 'r', 'g'], startangle=45, shadow=True, explode=(0, 0, 0.2), autopct='%1.2f%%')
plt.title(country)
plt.legend(loc='best', bbox_to_anchor=(0.8, 0, 0.3, 0.2))
plt.show()
