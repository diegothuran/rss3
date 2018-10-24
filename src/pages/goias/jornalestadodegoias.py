# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1, 10):
    if(i == 1):
        link = 'http://www.jornalestadodegoias.com.br/category/ultimas-noticias/'
    else:
        link = 'http://www.jornalestadodegoias.com.br/category/ultimas-noticias/page/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='td_block_wrap td_block_slide')
    noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='thumb-wrap')
    
    
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        print(href)
