# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1, 10):
    if(i == 1):
        link = 'https://diariodoestadogo.com.br/ultimas/'
    else:
        link = 'https://diariodoestadogo.com.br/ultimas/page/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='vw-block-grid-item')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        if('author' in href):
            pass
        else:
            print(href)
