'''
FilePath: forecast.py
Author: LiRunze
Date: 2022-08-23 02:00:44
LastEditors: LiRunze
LastEditTime: 2022-08-23 02:36:37
Description: 
'''

import time
import requests
import bs4

def getWeb(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    r = requests.get(url, headers=headers, timeout=30)
    content = r.text.encode('ISO-8859-1')
    return content

def getList(content):
    
    soup = bs4.BeautifulSoup(content, 'lxml')

    # 存放天气情况
    list_weather = []
    wrlist = soup.find_all('p', class_='wea')
    for weather in wrlist:
        list_weather.append(weather.text)
    
    # 存放日期
    list_day = []
    dlist = soup.find_all('h1')
    i = 0
    for day in dlist:
        if i <= 6:
            list_day.append(day.text.strip())
            i += 1
    
    # 存放温度
    list_temperture = []
    tlist = soup.find_all('p', class_='tem')
    i = 0
    for temperture in tlist:
        list_temperture.append([temperture.span.text, temperture.i.text])
        i += 1
    
    # 存放风力
    list_wind = []
    wdlist = soup.find_all('p', class_='win')
    for wind in wdlist:
        list_wind.append(wind.i.text.strip())

    return list_day, list_weather, list_temperture, list_wind

def getContent(url):
    
    content = getWeb(url)
    day, weather, temperture, wind = getList(content)
    datetimes = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    fname = "data/" + datetimes + r"_weather.txt"

    with open(fname, 'a+', encoding='utf-8') as file:
        for i in range(0,7):
            file.write(day[i]+":\t")
            file.write(weather[i]+"\t")
            file.write("最高气温:"+temperture[i][0]+"\t")
            file.write("最低气温:"+temperture[i][1]+"\t")
            file.write("风力:"+wind[i]+"\t")
            file.write("\n")

if __name__ == "__main__":
    url = "http://www.weather.com.cn/weather/101070201.shtml"
    getContent(url)
