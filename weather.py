#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An introduction to BeautifulSoup for Weather."""

import urllib2
from bs4 import BeautifulSoup

url = 'http://www.wunderground.com/history/airport/KNYC/2016/11/6/MonthlyCalendar.html'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")

def weather():
    """Some actual weather and some forcaste weather."""
    weather_list = []
    fhandler = soup.find_all('table', class_='dayTable')
    date = None
    
    for temps in fhandler:
        try:
            if date == None:
                date = temps.find('a', class_='dateText').text.strip()
                continue
            header = temps.find('td', class_='value-header', 
                                text=['Actual:', 'Forecast:'])

            if header != None:
                high = temps.find('span', class_='high').get_text()
                low = temps.find('span', class_='low').get_text()
                weather_list.append({
                    'Date': date,
                    'Header': header.text,
                    'High': high,
                    'Low': low
                    })
            
            date = None

        except:
            print 'This is corrupt'
            continue

    for final_weather in weather_list:
        print (final_weather['Date'] + '  '\
        + final_weather['Header'] + '  '\
        + final_weather['High'] + '  '\
        + final_weather['Low'])
    
    return weather_list

if __name__ == "__main__":
    weather()
