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



    exception = soup.find_all('tr', {'class': 'wi bot'})
    # ex = exception.find('tr', {'class': ['wi', 'wigr1']})
    #print(exception)

    for e in exception.previous_siblings:
        #print(e.next)
        print(e)

























    #
    # #Находим значения лучшей цены, отображенной наверху страницы
    # tr_wi = soup.find('tr', {'class': 'wi'})
    # tr_wi.td.decompose()
    # upper_best_courses = tr_wi.get_text()
    #
    # ubc = upper_best_courses.replace(',', '.')      # запятые прверащаем в точки
    # ubc = re.sub(r'[^0-9.]+', r' ', ubc)            # в одну строку помещаем
    # ubc = ubc.strip(' ')                            # убрали пробелы в начале и в конце
    # ubc = ubc.split(' ')                            # сделали список, использовав пробелы между числами, в качестве разделителя элементов списка
    # ubc = [float(chars) for chars in ubc]           # превратили элементы в списке в float
    #
    # print(ubc)
    #
    # # тут лучшие значения покупки/продажи доллара/евро (то что отмечено на сайте красным цветом)
    # b_k = soup.find_all('td', {'class': 'b-k'})
    #
    # length = len(b_k)
    # if length == 4:
    #     print('Все ровно по красным!')
    # else:
    #     print('Красных элементов не 4')
    #
    # bank_doll_sale = b_k[0].find_parent().find('a', {'class': 't-b'}).get_text()
    # bank_doll_buy = b_k[2].find_parent().find('a', {'class': 't-b'}).get_text()
    # bank_euro_buy = b_k[1].find_parent().find('a', {'class': 't-b'}).get_text()
    # bank_euro_sale = b_k[3].find_parent().find('a', {'class': 't-b'}).get_text()
    #
    # doll_sale = float(b_k[0].get_text().replace(',', '.'))
    # doll_buy = float(b_k[2].get_text().replace(',', '.'))
    # euro_buy = float(b_k[1].get_text().replace(',', '.'))
    # euro_sale = float(b_k[3].get_text().replace(',', '.'))
    #
    #
    # print(doll_buy, bank_doll_buy, doll_sale, bank_doll_sale, euro_buy, bank_euro_buy, euro_sale, bank_euro_sale)
    #
    #
    #
    #
    #









