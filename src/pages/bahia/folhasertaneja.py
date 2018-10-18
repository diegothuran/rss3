# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

root = 'http://www.folhasertaneja.com.br'
link = 'http://www.folhasertaneja.com.br/'

req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find_all('h3')
for noticia in noticias:
    href = noticia.find_all('a', href=True)[0]['href']
    full_link = root + href 
    print(full_link)
