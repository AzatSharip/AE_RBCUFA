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

    print(ubc)





    # banks = soup.find_all('tr', {'class': ['wi', 'wigr1']})
    #
    # #banks = soup.find_all('td', {'class': ['tbn top']})
    # print(banks)

    # for items in banks:
    #     print(items)

    value = soup.find_all('td', {'class': ['', 'top bot', 'b-k']})
    banks = soup.find_all('td', {'class': ['tbn top']})
    print('значений', len(value))
    print('банков', len(banks))




    val_list = list()
    val_dict = dict()
    for v in value:
        val_list.append(float(v.get_text().replace(',', '.')))
    for u in ubc:
        for val in val_list:
            if u == val:
                print(val)
                print(value[val_list.index(val)].parent('a', {'class': ['t-b']}))
                val_dict[val] = value[val_list.index(val)].parent('a', {'class': ['t-b']})


    print(val_dict)
    print()

    val_dict2 = dict()
    for key, value in val_dict.items():


        print(value)





    #     print(set(upper_best_courses).intersection(set(best_values_in_bank)))


# >>> a = [1, 3, 5, 7, 9]
# >>> b = [2, 4, 6, 8, 10]
# >>> list(zip(a, b))
# [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]




