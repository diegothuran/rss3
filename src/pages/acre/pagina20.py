# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1,10):
    if(i == 1):
        link = 'http://pagina20.net/v2/category/geral/'
    else:
        link = 'http://pagina20.net/v2/category/geral/page/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='card painel-noticias2')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
#         full_link = root + href 
        print(href)
