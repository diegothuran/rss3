# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

# categorias = [
#         'http://www.jornalatribuna.com.br/?cat=2',
#         'http://www.jornalatribuna.com.br/?cat=9',
#         'http://www.jornalatribuna.com.br/?cat=16',
#     ]

categorias = ['2', '9', '16']
for categoria in categorias:
    for i in range(1,10):
        if(i == 1):
            link = 'http://www.jornalatribuna.com.br/?cat=' + categoria
        else:
            link = 'http://www.jornalatribuna.com.br/?cat='+ categoria +'&paged=' + str(i)
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='entry-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
    #         full_link = root + href 
            print(href)
