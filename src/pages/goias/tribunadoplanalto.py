# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1, 10):
    if(i == 1):
        link = 'http://tribunadoplanalto.com.br/ultimas-noticias/'
    else:
        link = 'http://tribunadoplanalto.com.br/ultimas-noticias/page/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='td-module-thumb')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        print(href)
