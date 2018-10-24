# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

links = [
        'https://imirante.com/oestadoma/politica/',
    ]

for link in links:
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='article-timeline list-row')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        print(href)
