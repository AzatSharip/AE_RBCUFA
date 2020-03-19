import requests
import sys
from lxml import html
from bs4 import BeautifulSoup
import re

url = 'https://kovalut.ru/kurs/ufa/'
r = requests.get(url)
with open('best2.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf8'))

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

    print('Best buy and sell: ', ubc)


    #banks = soup.find_all('tr', {'class': ['wi', 'wigr1']})
    value = soup.find_all('td', {'class': ['', 'top bot', 'b-k']})
    banks = soup.find_all('td', {'class': ['tbn top']})

    val_list = list()
    best_dict = dict()

    for v in value:
        val_list.append(float(v.get_text().replace(',', '.')))
        #print(v)

    for u in ubc:
        for val in val_list:
            if u == val:
                bank_name = value[val_list.index(val)].parent('a', {'class': ['t-b']})
                bank_name = str(bank_name)
                bank_name = re.sub(r'.<a.*?>', '', bank_name).replace('</a>]', '')
                #print(val)
                #print(bank_name)
                best_dict[val] = bank_name





    print(best_dict)

    db_bank = best_dict.get(ubc[0])
    ds_bank = best_dict.get(ubc[1])
    eb_bank = best_dict.get(ubc[2])
    es_bank = best_dict.get(ubc[3])

    d_b = ubc[0]
    d_s = ubc[1]
    e_b = ubc[2]
    e_s = ubc[3]








