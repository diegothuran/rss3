# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

link = 'http://dc.clicrbs.com.br/sc/noticias/ultimas-noticias/'
req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='title')
for noticia in noticias:
    try:
        href = noticia.find_all('a', href=True)[0]['href']
        print(href)
    except: 
        pass
