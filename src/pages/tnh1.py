# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1,5):
    print(' --- ' + str(i))
    if(i == 1):
        link = 'https://www.tnh1.com.br/noticias/ultimas/'
    else:
        link = 'https://www.tnh1.com.br/noticias/ultimas/pagina/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='noticias-listagem__lista__item__image')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
    #     full_link = root + href 
        print(href)