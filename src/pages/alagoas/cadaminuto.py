# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

root = 'https://www.cadaminuto.com.br'
for i in range(1, 10):
    if(i == 1):
        link = 'https://www.cadaminuto.com.br/noticias'
    else:
        link = 'https://www.cadaminuto.com.br/noticias?page=' + str(i)
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='col-md-4')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        full_link = root + href 
        print(full_link)
