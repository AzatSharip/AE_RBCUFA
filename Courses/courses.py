import requests
import sys
from lxml import html
from bs4 import BeautifulSoup
#
# url = 'https://www.cbr.ru/'
# r = requests.get(url)
# with open('test.html', 'wb') as output_file:
#     output_file.write(r.text.encode('utf8'))

with open('test.html', 'rb') as output_file:
    text = output_file.read()

    soup = BeautifulSoup(text, features="lxml")

    d = soup.find('div', {'class': 'w_data_wrap'}).find('i').get('title')
    # c = soup.find('div', {'class': 'w_data_wrap'}).find('div').text
    # data_wrap = d.soup.find_all('i', {'class': 'up'})
    print(d)
    # print(c)


    # for d in d:
    #
    #     print(d)
    # items = doll_list.find_all('div', {'class': ['w_data_wrap']})
    # print(items)
    # for item in items:
    #     movie_link = (tag.name, tag.text)
    #     print(movie_link)

    # tree = html.fromstring(output_file)
    # tree.xpath








#sys.exit()

