from urllib.request import urlopen
import time

while True:
    try:
        urlopen("https://www.google.com/")
    except:
        print("Network down.")
        time.sleep(1)
    else:
        break
url = 'https://api.covid19api.com/'
