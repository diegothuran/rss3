# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

link = 'https://www.noticiaagora.com.br/'
req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='modulo')
for noticia in noticias:
    href = noticia.find_all('a', href=True)[0]['href']
    print(href)
