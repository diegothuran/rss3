# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

link = 'https://www.em.com.br/gerais/'
req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find_all('h4', class_='txt-serif mt-0 mb-10')
for noticia in noticias:
    href = noticia.find_all('a', href=True)[0]['href'] 
    print(href)
