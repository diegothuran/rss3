# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1,10):
    link = 'https://ne10.uol.com.br/radar/buscar/page:' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='listagemDeNoticia-item')
    for noticia in noticias:
        print(noticia.find_all('a', href=True)[0]['href'])

