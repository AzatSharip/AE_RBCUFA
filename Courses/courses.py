import requests
import sys
from lxml import html
from bs4 import BeautifulSoup

url = 'https://www.cbr.ru/'
r = requests.get(url)
with open('test.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf8'))

with open('test.html', 'rb') as output_file:
    soup = BeautifulSoup(output_file, features="lxml")
    doll_list = soup.find('div', {'class': 'content'})

    items = doll_list.find_all('div', {'class': ['w_data_wrap']})

    # for item in items:
    movie_link = doll_list.find('i', {'class': 'up'}).find('title').text



    print(movie_link)

    # tree = html.fromstring(output_file)
    # tree.xpath








sys.exit()

