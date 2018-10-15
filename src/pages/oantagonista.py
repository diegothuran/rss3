# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1,10):
    link = 'https://www.oantagonista.com/pagina/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='container-post-home')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[2]['href'] 
        print(href)