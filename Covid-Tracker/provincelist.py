import jsontodict as info

# Collects Data of Country and Provinces and Stores it
data = info.data['locations']
with open('province.txt', 'w') as file:
    country = ''
    for datum in data:
        country = datum['country']
        province = datum['province']
        file.write(country)
        file.write("-")
        if province.strip() == '':
            file.write(country)
        else:
            file.write(province)
        file.write('\n')