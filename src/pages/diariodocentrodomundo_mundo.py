# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

link = 'https://www.diariodocentrodomundo.com.br/mundo/'
req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='td_block_inner')
for noticia in noticias:
    href = noticia.find_all('a', href=True)[0]['href'] 
    print(href)
