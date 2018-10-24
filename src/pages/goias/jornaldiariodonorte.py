# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

# for i in range(1, 10):
#     if(i == 1):
#         link = 'http://www.jornaldiariodonorte.com.br/noticias/'
#     else:
#         link = 'http://www.jornaldiariodonorte.com.br/noticias/' + str(i)
link = 'https://www.jornalopcao.com.br/'
req = requests.get(link)
# noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='home-daily-slider')
noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='home-daily-featured-title')

for noticia in noticias:
    href = noticia.find_all('a', href=True)[0]['href'] 
    if('opcao-play' in href):
        pass
    else:
        print(href)
