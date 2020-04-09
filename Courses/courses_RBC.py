# С сайта РБК. Не доделано
import requests
from bs4 import BeautifulSoup
import datetime


url = 'https://ufa.rbc.ru/'
r = requests.get(url)
with open('rbc.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf8'))

with open('rbc.html', 'rb') as output_file:
    text = output_file.read()

    soup = BeautifulSoup(text, features="lxml")

    doll = soup.find_all('span', {'class': 'news-feed__item__title news-feed__item_bold'})
    euro = soup.find('span', {'class': 'news-feed__item__title news-feed__item_bold'})
    for d in doll:
        print(d)




