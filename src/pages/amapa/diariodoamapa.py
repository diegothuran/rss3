# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

link = 'https://aquiamapa.com.br/'
req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find('div', class_='footer-widget widget_recent_entries')

list_href = noticias.find_all('a', href=True)
for i in range(len(list_href)):
    print(list_href[i]['href'])
