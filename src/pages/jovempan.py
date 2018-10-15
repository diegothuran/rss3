# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

# root = 'https://www.gazetadopovo.com.br/'
for i in range(1, 10):
    if(i == 1):
        link = 'https://jovempan.uol.com.br/ultimas'
    else:
        link = 'https://jovempan.uol.com.br/ultimas/page/' + str(i)
        
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='post-title')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href'] 
        print(href)
