'''
FilePath: covid19_spider.py
Author: LiRunze
Date: 2022-08-22 22:59:38
LastEditors: LiRunze
LastEditTime: 2022-08-23 00:05:19
Description:
'''

from cgitb import html
import re
import requests
import time
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getContent(url):
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    paras_tmp = soup.select('.gk_title') + soup.select('p')
    paras = paras_tmp[0:]
    return paras

def saveFile(text):
    datetimes = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    fname = "data/" + datetimes + r"_data.txt"
    # fname = datetimes + r"_data.txt"
    f = open(fname, 'w')
    for t in text:
        if len(t) > 0:
            f.writelines(t.get_text() + "\n")
    f.close()

def main():
    url = 'https://www.bengbu.gov.cn/public/22601/49996408.html'
    text = getContent(url)
    saveFile(text)

main()

