from bs4 import BeautifulSoup
import requests

url='https://www.amazon.in/Python-Cookbook-Brian-Jones/dp/9351101401/ref=sr_1_2?keywords=cookbook+python&qid=1568016749&s=gateway&sr=8-2'
headers= {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
src= requests.get(url, headers=headers).text


soup=BeautifulSoup(src,'html.parser')
# print(soup.prettify())
title=soup.find(id='productTitle')
print(title.text)
price= soup.find(class_='a-size-base a-color-price a-color-price')
print(price.text.strip())
