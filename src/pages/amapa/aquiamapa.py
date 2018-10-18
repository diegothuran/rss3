# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1, 10):
    print(' --------' + str(i))
    if(i == 1):
        link = 'https://www.diariodoamapa.com.br/category/cadernos/ultima-hora/'
    else:
        link = 'https://www.diariodoamapa.com.br/category/cadernos/ultima-hora/page/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col col-xs-12 col-sm-9 col-md-9')
    
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
#         full_link = root + href 
        print(href)
