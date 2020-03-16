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

    print(upper_best_courses)


    #banks = soup.find_all('tr', {'class': ['wi', 'wigr1']})
    banks = soup.find_all('td', {'class': ['', 'top bot']})

    # for values in banks:
    #     best_values_in_bank = values.get_text()
    #     print(set(upper_best_courses).intersection(set(best_values_in_bank)))






    # print(banks)
