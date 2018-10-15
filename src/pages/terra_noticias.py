# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

link = 'https://www.terra.com.br/noticias'
req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find_all('h3')
for noticia in noticias:
    href = noticia.find_all('a', href=True)[0]['href'] 
    print(href)
