# Курсы с сайта banki.ru. Рабочая версия. Отказались потому что парсит данные только на текущий день.
import requests
from bs4 import BeautifulSoup
import datetime


url = 'https://www.banki.ru/products/currency/cb/'
r = requests.get(url)
with open('banki.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf8'))

with open('banki.html', 'rb') as output_file:
    text = output_file.read()

    soup = BeautifulSoup(text, features="lxml")

    doll = soup.find('tr', {'data-currency-code': 'USD'})
    doll.td.decompose()
    doll.td.decompose()
    doll.td.decompose()
    doll_val = doll.find_all('td')[0].get_text()
    doll_val = float(doll_val)
    doll_val = round(doll_val, 2)

    euro = soup.find('tr', {'data-currency-code': 'EUR'})
    euro.td.decompose()
    euro.td.decompose()
    euro.td.decompose()
    euro_val = euro.find_all('td')[0].get_text()
    euro_val = float(euro_val)
    euro_val = round(euro_val, 2)

    doll_dynamics_dirty = doll.find('td', {'class': ['color-red', 'color-green']}).get_text()
    euro_dynamics_dirty = euro.find('td', {'class': ['color-red', 'color-green']}).get_text()

    def clear_dyn(dyn):
        try:
            if '-' in dyn:
                dyn = dyn.replace(',', '.')
                dyn = dyn.replace('-', '')
                dyn = float(dyn)
                dyn = round(dyn, 2)
                arrow = 100
                return dyn, arrow
            elif '+' in dyn:
                dyn = dyn.replace(',', '.')
                dyn = dyn.replace('+', '')
                dyn = float(dyn)
                dyn = round(dyn, 2)
                arrow = 0
                return dyn, arrow
        except: print('Something wrong with module CLEAR_DYN')


    doll_dynamics, doll_arrow = clear_dyn(doll_dynamics_dirty)
    euro_dynamics, euro_arrow = clear_dyn(euro_dynamics_dirty)

    today = datetime.datetime.today()
    day = today.strftime("%d")
    month = today.strftime("%m")
    month_dict = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
                  '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
                  }
    for keys in month_dict:
        if month == keys:
            month = month_dict[keys]

    date = day + ' ' + month

    print(date)
    print(doll_val)
    print(doll_dynamics)
    print(doll_arrow)
    print()
    print(euro_val)
    print(euro_dynamics)
    print(euro_arrow)





