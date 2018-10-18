# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

root = 'http://www.tribunafeirense.com.br'
links = [
        'http://www.tribunafeirense.com.br/secoes/1/1/geral',
        'http://www.tribunafeirense.com.br/secoes/2/1/bahia',
        'http://www.tribunafeirense.com.br/secoes/3/1/brasil',
        'http://www.tribunafeirense.com.br/secoes/4/1/politica',
        'http://www.tribunafeirense.com.br/secoes/7/1/economia',
        'http://www.tribunafeirense.com.br/secoes/10/1/famosos',
        'http://www.tribunafeirense.com.br/secoes/20/1/mundo'
    ]

for link in links:    
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='titulo2')
    
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        full_link = root + href     
        print(full_link)
