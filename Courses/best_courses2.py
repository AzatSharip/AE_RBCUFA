import requests
import sys
from lxml import html
from bs4 import BeautifulSoup
import re

# url = 'https://kovalut.ru/kurs/ufa/'
# r = requests.get(url)
# with open('best2.html', 'wb') as output_file:
#     output_file.write(r.text.encode('utf8'))

with open('best2.html', 'rb') as output_file:
    text = output_file.read()
    soup = BeautifulSoup(text, features="lxml")

    #Находим значения лучшей цены, отображенной наверху страницы
    tr_wi = soup.find('tr', {'class': 'wi'})
    tr_wi.td.decompose()
    upper_best_courses = tr_wi.get_text()

    ubc = upper_best_courses.replace(',', '.')      # запятые прверащаем в точки
    ubc = re.sub(r'[^0-9.]+', r' ', ubc)            # в одну строку помещаем
    ubc = ubc.strip(' ')                            # убрали пробелы в начале и в конце
    ubc = ubc.split(' ')                            # сделали список, использовав пробелы между числами, в качестве разделителя элементов списка
    ubc = [float(chars) for chars in ubc]           # превратили элементы в списке в float

    #print(ubc)



    # banks = soup.find_all('tr', {'class': ['wi', 'wigr1']})
    #
    # #banks = soup.find_all('td', {'class': ['tbn top']})
    # print(banks)

    # for items in banks:
    #     print(items)

    value = soup.find_all('td', {'class': ['', 'top bot']})
    banks = soup.find_all('td', {'class': ['tbn top']})




    def bank_value(bank, value):
        bv = dict()
        for b in bank:
            for v in value:
                bv[b] = v
        return bv

    #print(bank_value(banks, value))





    #     print(set(upper_best_courses).intersection(set(best_values_in_bank)))







