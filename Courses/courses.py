import requests
import sys
from lxml import html
from bs4 import BeautifulSoup
import re

url = 'https://www.cbr.ru/'
r = requests.get(url)
with open('cbrf.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf8'))

with open('cbrf.html', 'rb') as output_file:
    text = output_file.read()

    soup = BeautifulSoup(text, features="lxml")
    #print(soup.prettify())

    doll = soup.find_all('div', {'class': 'w_data_wrap'})[0]
    euro = soup.find_all('div', {'class': 'w_data_wrap'})[1]

    # Находим динамику доллара и евро
    doll_dynamics = doll.find('i').get('title')
    euro_dynamics = euro.find('i').get('title')

    #Находим стоимость доллара
    doll.ins.decompose()
    doll.i.decompose()
    for i in doll:
        doll_val = i

    # Находим стоимость евро
    euro.ins.decompose()
    euro.i.decompose()
    for i in euro:
        euro_value = i

    #Вычленяем дату
    # content = soup.find_all('div', {'class': 'content'})[2]
    widget = soup.find('div', {'id': 'widget_exchange'})
    content = widget.find('div', {'class': 'content'})
    date = content.find_all('a')[1].get_text()


    print('Курсы валют установленные ЦБ РФ на {}'.format(date))
    print('Доллар -- Стоимость: {}, динамика: {}'.format(doll_val, doll_dynamics))
    print('Евро -- Стоимость: {}, динамика: {}'.format(euro_value, euro_dynamics))













#sys.exit()



# doll_dynamics = soup.find('div', {'class': 'w_data_wrap'})
#     doll_dynamics.ins.decompose()
#     doll_dynamics.i.decompose()
#     for i in doll_dynamics:
#         print(i)


#doll_dynamics = soup.find('div', {'class': 'w_data_wrap'}).find('i').get('title')