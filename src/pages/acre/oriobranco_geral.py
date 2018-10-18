# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

root = 'http://www.oriobranco.net/'
for i in range(1,10):
    if(i == 1):
        link = 'http://www.oriobranco.net/geral'
    else:
        link = 'http://www.oriobranco.net/geral/pagina/' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='destaque-thumb foto clearfix')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        full_link = root + href 
        print(full_link)
