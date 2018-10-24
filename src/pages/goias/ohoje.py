# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

root = 'http://www.ohoje.com.br'
# for i in range(10):
#     if(i == 0):
#         link = 'https://www.gazetadopovo.com.br/ultimas-noticias/'
#     else:
#         link = 'https://www.gazetadopovo.com.br/ultimas-noticias/?offset=' + str(i)
req = requests.get(root)
noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='pltc')
for noticia in noticias:
    href = noticia.find_all('a', href=True)[0]['href']
    full_link = root + href 
    print(full_link)
