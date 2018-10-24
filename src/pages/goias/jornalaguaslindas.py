# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

# root = 'https://www.gazetadopovo.com.br/'
# for i in range(10):
#     if(i == 0):
#         link = 'https://www.gazetadopovo.com.br/ultimas-noticias/'
#     else:

links = [
        'http://www.jornalaguaslindas.com.br/search/label/Cidade',
        'http://www.jornalaguaslindas.com.br/search/label/Distrito%20Federal',
        'http://www.jornalaguaslindas.com.br/search/label/Goi%C3%A1s',
        'http://www.jornalaguaslindas.com.br/search/label/Mundo',
        'http://www.jornalaguaslindas.com.br/search/label/Pol%C3%ADtica',
        'http://www.jornalaguaslindas.com.br/search/label/policia'
    ]

for link in links:
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='post-outer')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        print(href)
