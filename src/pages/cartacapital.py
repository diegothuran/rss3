# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

# link = 'https://www.cartacapital.com.br/ultimas-noticias'
pages_idx = ['0', '30', '60']
for i in range(len(pages_idx)):
#     print('------------ ' + str(pages_idx[i]))
    if(i == 0):
        link = 'https://www.cartacapital.com.br/ultimas-noticias'
    else:
        link = 'https://www.cartacapital.com.br/ultimas-noticias?b_start:int=' + pages_idx[i] 
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='tileHeadline')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href'] 
        print(href)
