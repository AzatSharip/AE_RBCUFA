import requests
import sys
from lxml import html
from bs4 import BeautifulSoup
import re

url = 'https://kovalut.ru/kurs/ufa/'
r = requests.get(url)
with open('best.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf8'))

with open('best.html', 'rb') as output_file:
    text = output_file.read()
    soup = BeautifulSoup(text, features="lxml")

    # тут лучшие значения покупки/продажи доллара/евро (то что отмечено на сайте красным цветом)
    b_k = soup.find_all('td', {'class': 'b-k'})

    length = len(b_k)
    if length == 4:
        print('Все ровно по красным!')
    else:
        print('Красных элементов не 4')

    bank_doll_sale = b_k[0].find_parent().find('a', {'class': 't-b'}).get_text()
    bank_doll_buy = b_k[2].find_parent().find('a', {'class': 't-b'}).get_text()
    bank_euro_buy = b_k[1].find_parent().find('a', {'class': 't-b'}).get_text()
    bank_euro_sale = b_k[3].find_parent().find('a', {'class': 't-b'}).get_text()

    doll_sale = b_k[0].get_text()
    doll_buy = b_k[2].get_text()
    euro_buy = b_k[1].get_text()
    euro_sale = b_k[3].get_text()


    print(doll_buy, bank_doll_buy, doll_sale, bank_doll_sale, euro_buy, bank_euro_buy, euro_sale, bank_euro_sale)




    # for items in b_k:
    #     print(items.get_text())






        # print(item.find_parent().find('a', {'class': 't-b'}).get_text())
        # print(item.get_text())








