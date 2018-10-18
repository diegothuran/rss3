# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

root = 'https://novoextra.com.br'
links = [
        'https://novoextra.com.br/so-no-site/alagoas',
        'https://novoextra.com.br/so-no-site/geral',
        'https://novoextra.com.br/so-no-site/internacional',
        'https://novoextra.com.br/so-no-site/nacional',
        'https://novoextra.com.br/so-no-site/politica'
        ]


for link in links:
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='item')
    for noticia in noticias:    
        href = noticia.find_all('a', href=True)[0]['href']
        full_link = root + href 
        print(full_link)
        
