# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1,10):
    if(i == 1):
        link = 'https://www.oaltoacre.com/ultimas-noticias/'
    else:
        link = 'https://www.oaltoacre.com/ultimas-noticias/page/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title td-module-title')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
#         full_link = root + href 
        print(href)
