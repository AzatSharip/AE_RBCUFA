import requests
from bs4 import BeautifulSoup


url = 'http://old.cbr.ru/'
r = requests.get(url)
with open('cbrf.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf8'))

with open('cbrf.html', 'rb') as output_file:
    text = output_file.read()

    soup = BeautifulSoup(text, features="lxml")

    doll = soup.find_all('div', {'class': 'w_data_wrap'})[0]
    euro = soup.find_all('div', {'class': 'w_data_wrap'})[1]

    # Находим динамику доллара и евро
    doll_dynamics = doll.find('i').get('title')
    euro_dynamics = euro.find('i').get('title')

    # Находим стоимость доллара
    doll.ins.decompose()
    doll.i.decompose()
    for i in doll:
        doll_val = i

    # Находим стоимость евро
    euro.ins.decompose()
    euro.i.decompose()
    for i in euro:
        euro_val = i

    # Вычленяем дату
    widget = soup.find('div', {'id': 'widget_exchange'})
    content = widget.find('div', {'class': 'content'})
    date = content.find_all('a')[1].get_text()

    date_split = date.split('.')
    month_dict = {'01' : 'января', '02' : 'февраля', '03' : 'марта', '04' : 'апреля', '05' : 'мая', '06' : 'июня',
                  '07' : 'июля', '08' : 'августа', '09' : 'сентября', '10' : 'октября', '11' : 'ноября', '12' : 'декабря'
                    }
    day = date_split[0]
    day = str(day)
    month = month_dict[date_split[1]]
    month = str(month)
    date = day + ' ' + month
    print("Делаем курсы валют на", date)

    # В динамике роста/падения перед числом стоит "+" или "-". Очищаем от этих символов.
    if doll_dynamics.startswith('-') == True:
        doll_dynamics = doll_dynamics.replace('- ', '')
        doll_dynamics = doll_dynamics.replace(',', '.')
        doll_dynamics_arrow = 100
    else:
        doll_dynamics = doll_dynamics.replace('+ ', '')
        doll_dynamics = doll_dynamics.replace(',', '.')
        doll_dynamics_arrow = 0


    if euro_dynamics.startswith('-') == True:
        euro_dynamics = euro_dynamics.replace('- ', '')
        euro_dynamics = euro_dynamics.replace(',', '.')
        euro_dynamics_arrow = 100
    else:
        euro_dynamics = euro_dynamics.replace('+ ', '')
        euro_dynamics = euro_dynamics.replace(',', '.')
        euro_dynamics_arrow = 0

    # Переводим во флоат и округляем
    doll_dynamics = round(float(doll_dynamics), 2)
    euro_dynamics = round(float(euro_dynamics), 2)

    doll_val = round(float(doll_val.replace(',', '.')), 2)
    euro_val = round(float(euro_val.replace(',', '.')), 2)
