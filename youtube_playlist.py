from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time

b= webdriver.Chrome(executable_path=r'D:/chrome downloads/chromedriver_win32/chromedriver.exe')
b.get('https://keepvid.pro/')

r = requests.get('https://www.youtube.com/playlist?list=PLfBJlB6T2eOslbxvkGT4Ws5AGT1ewUEb9')
page = r.text
soup=bs(page,'lxml')
# print(soup.prettify())
res=soup.find_all('a',{'class':'pl-video-title-link'})
for l in res:
    print(l.text.strip())
    url=l['href']
    url=url.split('&')
    link=f'https://www.youtube.com{url[0]}'

    e= b.find_element_by_id('videourl')
    e.clear()
    e.send_keys(link)
    s=b.find_element_by_id('downloadbtn')
    s.click()
    time.sleep(10)
    d=b.find_element_by_id('best-download-btn')
    d.click()
    time.sleep(15)
    print(link)
