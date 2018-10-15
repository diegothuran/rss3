# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1,10):
    link = 'https://www.correio24horas.com.br/noticias/pagina/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='noticias-listagem--item-meta')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href'] 
        print(href)