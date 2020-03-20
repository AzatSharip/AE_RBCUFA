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
    print('Exception banks list:', exception_list)


    banks = soup.find_all('a', {'class': ['t-b']})
    print('Banks: ', len(banks))

    # extra = soup.find_all(class_='upd-t top bot')
    # for ex in extra:
    #     ex.decompose()
    #
    # extra2 = soup.find_all(class_='tbn top bot')
    # for ex in extra2:
    #     ex.decompose()


    #
    # value_rowspan = soup.find_all('td', {'rowspan': '2'})
    # value_top_bot = soup.find_all('td', {'class': 'top bot'})
    # value = value_rowspan + value_top_bot
    #
    # print(len(value))
    # for v in value:
    #     print(v.parent.get_text())

    banks = soup.find_all('tr', {'class': ['wi', 'wigr1']})
    dec = soup.find(class_ = 'wigr1 bot')

    elem = list()
    for b in banks:
        content = b.get_text()
        content = content.strip(' ')
        content = content.strip('\xa0')
        content = content.split('\n')
        elem.append(content)
        # print(content)

    [e.remove('') for e in elem]
    elements = list()
    for e in elem:
        elements.append(e[0:5])

#Очищаем список от шлака, оставляем только банки и цены покупки/продажи
    for e in elements:
        if len(e) < 5:
            i = elements.index(e)
            elements.pop(i)
    elements.pop(0)

#Удаляем из списка все банки - исключения
    for ex in exception_list:
        for e in elements:
            if ex in e:
                i = elements.index(e)
                elements.pop(i)

# Создаем словари, где ключи - название банка, а значения - стоимость продажи или покупки
    elements2 = list()
    db = dict()
    ds = dict()
    eb = dict()
    es = dict()
    for e in elements:
        e = [e.replace(',', '.') for e in e]
        db[float(e[1])] = e[0]
        ds[float(e[2])] = e[0]
        eb[float(e[3])] = e[0]
        es[float(e[4])] = e[0]

    doll_buy = min(db)
    doll_buy_b = db[doll_buy]

    doll_sale = max(ds)
    doll_sale_b = ds[doll_sale]

    euro_buy = min(eb)
    euro_buy_b = eb[euro_buy]

    euro_sale = max(es)
    euro_sale_b = es[euro_sale]



    print(doll_buy, doll_buy_b, doll_sale, doll_sale_b, euro_buy, euro_buy_b, euro_sale, euro_sale_b)






    # print(doll_buy, doll_buy_bank, doll_sale)






    #
    # print(db)
    # print(ds)
    # print(eb)
    # print(es)
    # print(len(db))
































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









