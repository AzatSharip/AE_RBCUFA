
import requests
url = 'https://informer.kovalut.ru/webmaster/getxml.php?kod=0201'
r = requests.get(url)
print(r)