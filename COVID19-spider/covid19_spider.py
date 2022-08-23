'''
FilePath: covid19_spider.py
Author: LiRunze
Date: 2022-08-22 22:59:38
LastEditors: LiRunze
LastEditTime: 2022-08-23 01:40:19
Description:
'''

from cgitb import html
from email import header
import re
import requests
import time
from bs4 import BeautifulSoup

def getHTML(url, headers):
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getContent(url, headers):
    html = getHTML(url, headers)
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
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    text = getContent(url, headers)
    saveFile(text)

main()

