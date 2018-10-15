# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

link = 'https://veja.abril.com.br/ultimas-noticias/'

# for i in range(1,10):
#     if(i == 1):
#         link = 'https://www.istoedinheiro.com.br/ultimas/'
#     else:
#         link = 'https://www.istoedinheiro.com.br/ultimas/page/' + str(i)
req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='list-item')
for noticia in noticias:
    print(noticia.find_all('a', href=True)[0]['href'])
