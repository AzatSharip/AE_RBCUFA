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


    exception_list = list()
    #exception = soup.find_all('tr', {'class': 'wi bot'})
    ex = soup.find_all('tr', {'class': ['wi', 'wigr1']})

#Лист исключения. Эти банки не берем, потому что у них есть условия и комиссии
    for e in ex:
        if 'комиссия' in e.text:
            exc_bank = e.find_previous_sibling("tr")
            exc_bank = exc_bank.find('a', {'class': ['t-b']})
            exc_bank = str(exc_bank)
            exc_bank = re.sub(r'<a.*?>', '', exc_bank).replace('</a>', '')
            exception_list.append(exc_bank)
        elif 'обмен только' in e.text:
            ex_bank = e.find_previous_sibling("tr")
            ex_bank = ex_bank.find('a', {'class': ['t-b']})
            ex_bank = str(ex_bank)
            ex_bank = re.sub(r'<a.*?>', '', ex_bank).replace('</a>', '')
            exception_list.append(ex_bank)
    #print(exception_list)

    value = soup.find_all('td', {'class': ['', 'top bot', 'b-k']}, {'rowspan': '2'})
    banks = soup.find_all('td', {'class': ['tbn top']})

    for v in value:
        #print(v.find_previous_sibling("td"))
        print(v)




























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









