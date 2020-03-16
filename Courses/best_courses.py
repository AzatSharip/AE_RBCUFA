import requests
import sys
from lxml import html
from bs4 import BeautifulSoup
import re

# url = 'https://kovalut.ru/kurs/ufa/'
# r = requests.get(url)
# with open('best.html', 'wb') as output_file:
#     output_file.write(r.text.encode('utf8'))

with open('best.html', 'rb') as output_file:
    text = output_file.read()
    soup = BeautifulSoup(text, features="lxml")

    # тут лучшие значения покупки/продажи доллара/евро
    b_k = soup.find_all('td', {'class': 'b-k'})

    bank_doll_buy = b_k[0].find_parent().find('a', {'class': 't-b'}).get_text()
    bank_doll_sale = b_k[2].find_parent().find('a', {'class': 't-b'}).get_text()
    bank_euro_buy = b_k[1].find_parent().find('a', {'class': 't-b'}).get_text()
    bank_euro_sale = b_k[3].find_parent().find('a', {'class': 't-b'}).get_text()

    doll_buy = b_k[0].get_text()
    doll_sale = b_k[2].get_text()
    euro_buy = b_k[1].get_text()
    euro_sale = b_k[3].get_text()

    print(doll_buy, bank_doll_buy, doll_sale, bank_doll_sale, euro_buy, bank_euro_buy, euro_sale, bank_euro_sale)



        # print(item.find_parent().find('a', {'class': 't-b'}).get_text())
        # print(item.get_text())






        # var comp1 = ["на 16 марта", "73,19", "0,84", "81,86", "1,80"];
        # var doll_minus = ["100"];
        # var euro_minus = ["100"];
        #
        # var copm_doll = ["72,41", "банк финам", "73,06", "банк финам"];
        # var comp_euro = ["80,86", "банк финам", "81,53", "банк финам"];


