import requests
import sys
from lxml import html
from bs4 import BeautifulSoup

# url = 'https://www.cbr.ru/'
# r = requests.get(url)
# with open('test.html', 'wb') as output_file:
#     output_file.write(r.text.encode('utf8'))

with open('test.html', 'rb') as output_file:
    text = output_file.read()

    soup = BeautifulSoup(text, features="lxml")

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
    date = soup.find_all('div', {'class': 'content'})
    a = date.find('th', {'class': 'title'})
    # for d in date:
    #     a = d.find_all('th', {'class': 'title'})
    # date = date.find('span', {'class': 'nowrap'})
    print(a)

    # for i in date:
    #     date = i

    # #Убираем лишний текст из даты
    # indx = date.index(' ')
    # date = date[indx:]
    #
    #
    # print('Курсы валют установленные ЦБ РФ на{}'.format(date))
    # print('Доллар -- Стоимость: {}, динамика: {}'.format(doll_val, doll_dynamics))
    # print('Евро -- Стоимость: {}, динамика: {}'.format(euro_value, euro_dynamics))













#sys.exit()



# doll_dynamics = soup.find('div', {'class': 'w_data_wrap'})
#     doll_dynamics.ins.decompose()
#     doll_dynamics.i.decompose()
#     for i in doll_dynamics:
#         print(i)


#doll_dynamics = soup.find('div', {'class': 'w_data_wrap'}).find('i').get('title')