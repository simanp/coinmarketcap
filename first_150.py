import requests
from bs4 import BeautifulSoup
import csv
r = requests.get('https://coinmarketcap.com/all/views/all/')
soup = BeautifulSoup(r.text, 'lxml')

#收集前150个币
address = []
table = soup.find('table', id='currencies-all')
for row in table.find_all('tr'):
    try:
        symbol = row.find('a', class_='price').attrs

    except AttributeError:
        continue
    address.append(['https://coinmarketcap.com'+symbol['href']])
with open("website_cryptomarket.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(address[:150])
