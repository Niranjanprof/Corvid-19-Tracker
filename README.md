# Covid Tracker 

Covid Data Tracker

![Logo](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/logo.png)
---
## Current Tracker


![Covid-19 Confirmed](https://covid19-badges.herokuapp.com/confirmed/latest)                             ![Covid-19 Deaths](https://covid19-badges.herokuapp.com/deaths/latest)


___
The Python Code for getting Track of Novel Covid Pandemic growth in all over the world

__Tracks__ and __Visualize__ __data__ on patients,death,recovery in __line plots__ and __pie charts__

The project has three versions working on 2 diffrent APIs and on web scrapping choose between them according to your need 



The __[Abstract](Abstract.pdf)__ of this project has details about developement space of the project

---

## Our Website

Details about the __[Project](https://github.com/Niranjanprof/Covid-19-Tracker)__ ,__[WHO Guidelines](https://meenakshi2604.github.io/Covid-tracker/)__ and __[Chatbot](https://t.me/VisCoTbot)__ are available in our 
__[website VisCoT](https://meenakshi2604.github.io/Covid-tracker/)__

---

## Set-Up

```bash
$ pip install -r requirements.txt
```
---
# [Covid Tracker](CovidTracker) 

## Web Scrapping

The **[Website](worldometers.info)** we used


---

<ol>
<li>Runs with Web Scrapping</li>
<li>Fast Working</li>
<li>Reliable data on all affected countries than other API's</li>
<li>Total population of a Country is present</li>
<li>Various Ratio's are available</li>
<li>Latitude Longitude details are not available</li>
</ol>

---

## Working

<ul>
Refer .txt files while giving inputs
</ul>

| Result | File | command|
|--------|------|--------|
|Affected Country list |      [Country.txt](CovidTracker/Country.txt)||
|To get updates in Confirmed/Death/Recovered details of a country in a faster way |      [country.py](CovidTracker/country.py)|``` python3 country.py ```|
|Country Url list [country.py](CovidTracker/country.py) depends on this | [countryurl.txt](CovidTracker/countryurl.txt)||
|To get detailed Updates based on Countries like Population,Total Cases,New Cases,Total Deaths,New Deaths,Total Recovered,Active Cases,Serious,Critical,Tot Cases/1M pop,Deaths/1M pop,TotalTests,Tests/1M pop| [details.py](CovidTracker/details.py)|``` python3 details.py ```|
|To get static population data works along with details.py| [population.py](CovidTracker/populations.py)|```python3 populations.py```|
|To get Available Country list which can help you in choosing inputs for [details.py](CovidTracker/details.py)|      [filefordetails.txt](CovidTracker/filefordetails.txt)||
|To get Latest Global data |      [latest.py](CovidTracker/latest.py)|``` python3 latest.py ```|
|Whole Country list in the world|      [map.txt](CovidTracker/map.txt)||
|Population list run [population.py](CovidTracker/population.py) to get this filled  |      [population.txt](CovidTracker/population.txt)||
|To get population data | [population.py](CovidTracker/population.py)|```python3 population.py```|



---
# [Covid Tracker 1](CovidTracker1)

## API

The **[API](https://coronavirus-tracker-api.herokuapp.com/v2/locations)** we used

The **[Repo](https://github.com/ExpDev07/coronavirus-tracker-api)** api provider

---

<ol>
<li>Runs with slower Api</li>
<li>Province wise Detail-Analysis</li>
<li>Total population of a Country is present</li>
<li>Patient Recovery Details is not available</li>
</ol>

---

## Working

<ul>
Refer country.txt & province.txt while giving inputs

If they gets tampered run [countrylist.py](CovidTracker1/countrylist.py) , [provincelist.py](CovidTracker1/provincelist.py) respectively to regenrate them.

Do the same to update the lists
</ul>

| Result | File | command|
|--------|------|--------|
|To get latest Global updates |      [latest.py](CovidTracker1/latest.py)|``` python3 latest.py ```|
|To get Graphs on Result |      [timeline.py](CovidTracker1/timeline.py)|``` python3 timeline.py ```|
|To get Updates based on Country | [country.py](CovidTracker1/country.py)|``` python3 country.py ```|
|To get Updates based on Provinces | [province.py](CovidTracker1/provinces.py)|``` python3 province.py ```|
|To get Available Country list |      [countrylist.py](CovidTracker1/countrylist.py)|``` python3 countrylist.py ```|
|To get Available Province list |      [provincelist.py](CovidTracker1/provincelist.py)|``` python3 provincelist.py ```|
|Country list |      [country.txt](CovidTracker1/country.txt)||
|Province list |      [province.txt](CovidTracker1/province.txt)||
|To Convert json to dictionary | [jsontodict.py](CovidTracker1/jsontodict.py)||


---


# [Covid Tracker 2](CovidTracker2)

## API

The **[API](https://api.covid19api.com/)** we used

The **[Repo](https://github.com/CSSEGISandData/COVID-19)** api provider

---

<ol>
<li>Comparitively Much Faster Api</li>
<li>No  Province wise Details</li>
<li>Recovery number is  available</li>
<li>No data on Total population of a Country</li>
</ol>

---

## Working


<ul>
Refer country.txt while giving inputs

If it gets tampered run [countrylist.py](CovidTracker2/countrylist.py) to regenrate it.

Do the same to update the list
</ul>


| Result | File | command|
|--------|------|--------|
|To get latest Global updates |      [latest.py](CovidTracker2/latest.py)|``` python3 latest.py ```|
|To get Graphs on Result |      [timeline.py](CovidTracker2/timeline.py)|``` python3 timeline.py ```|
|To get Updates based on Country | [country.py](CovidTracker2/country.py)|``` python3 country.py ```|
|To get Available Country list |      [countrylist.py](CovidTracker2/countrylist.py)|``` python3 countrylist.py ```|
|Country list |      [country.txt](CovidTracker2/country.txt)||
|To Check connection ad to store url | [url.py](CovidTracker2/jsontodict.py)||



---



## Graph Plotting

### Line plot

Line graphs are plotted using matplotlib module
According to Provinces and Country Coresponding Graphs are produced

|![No. of Confirmed Cases](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/1%20(2).png)|![No. of Death Cases](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/1%20(1).png)|![No. of Recoverd Cases](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/1%20(4).png)|
|------------------------|-------------------------|------------------------|
|No. of Confirmed Cases|No. of Death Cases|No. of Recoverd Cases|

---



---

### Pie Plot

Pie charts are plotted using matplotlib.pyplot.pie function
According to Provinces and Country and Global details Coresponding Graphs are produced


|![Global](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/1.png)|![Country Specific](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/2.png)|![Country-Province](https://github.com/Niranjanprof/Covid-19-Tracker/blob/master/rsc/3.png)|
|------------------------|-------------------------|------------------------|
|Global|Country Specific|Country-Province|

---
## Task

<ul>
  <li>'travis.yml' build status development.</li> 
  <li>Unicode fixes</li>
  <li>Adding Ratio's</li> 
</ul>

---

## Contributors


<table>
  <tr>
    <td align="center"><a href="https://github.com/Niranjanprof"><img src="https://avatars1.githubusercontent.com/u/48713926?s=400&u=a473cb9bbbc98506ae6b55ccd2b45cfdc941d517&v=4" width="200px;" alt=""/><br /><sub><b>Niranjan B(Prof Moriarty)</b></sub></a><br /><a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=Niranjanprof" title="Code">💻</a> <a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=Niranjanprof" title="Documentation">📖</a> <a href="#maintenance-Niranjanprof" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/AJITH-klepsydra"><img src="https://avatars3.githubusercontent.com/u/62293152?s=400&v=4" width="200px;" alt=""/><br /><sub><b>Ajith PM(Klepsydra Alpha)</b></sub></a><br /><a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=AJITH-klepsydra" title="Code">💻</a> <a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=AJITH-klepsydra" title="Documentation">📖</a></td>
  <td align="center"><a href="https://github.com/amalnathm7https://github.com/Meenakshi2604"><img src="https://avatars2.githubusercontent.com/u/64605131?s=400&u=7263b2b702f0175dff070e379d065557f6843a85&v=4" width="200px;" alt=""/><br /><sub><b>Amal Nath(Dr.Strange)</b></sub></a><br /><a href="https://github.com/Niranjanprof/Corvid-19-Tracker/commits?author=amalnathm7" title="Documentation">📖</a></td>
  </tr>
  <tr>
  <td align="center"><a href="https://github.com/Meenakshi2604"><img src="https://avatars3.githubusercontent.com/u/62795103?s=400&v=4" width="200px;" alt=""/><br /><sub><b>Meenakshi Nair(Meenu)</b></sub></a><br /><a href="https://meenakshi2604.github.io/Covid-tracker/" title="Web Designer">💻</a></td>
  <td align="center"><a href="https://github.com/Sinadin-Shibin"><img src="https://avatars3.githubusercontent.com/u/59430074?s=400&v=4" width="200px;" alt=""/><br /><sub><b>Sinadin Shibin (Skeptic)</b></sub></a><br /><a href="https://github.com/Sinadin-Shibin" title="Code">💻</a></td>
  <td align="center"><a href="https://github.com/Dinoy-Raj"><img src="https://avatars2.githubusercontent.com/u/62199728?s=400&u=ec49e70797755f5091bcc1cd3ee60f5faaec91b6&v=4" width="200px;" alt=""/><br /><sub><b>Dinoy Raj
(Raj)</b></sub></a><br /><a href="https://github.com/Dinoy-Raj" title="Logo Designer">📊</a></td>
  </tr>

</table>

---

## License & copyright

© Niranjan B 
,Ajith PM

Licensed under the [GNU GPL](LICENSE)

---

Mention This [Repo](https://github.com/Niranjanprof/Covid-19-Tracker) while you use this in your projects :)
