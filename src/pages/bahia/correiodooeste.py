# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests


link = 'http://correiodooeste.com.br/'

req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_="row news-blog")

for noticia in noticias:
    href = noticia.find_all('a', href=True)[0]['href']
    print(href)