# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

links = [
    'https://imirante.com/oestadoma/politica/',
    'https://imirante.com/oestadoma/economia/',
    'https://imirante.com/oestadoma/cidades/',
    'https://imirante.com/oestadoma/o-mundo/',
    'https://imirante.com/oestadoma/o-pais/',
    'https://imirante.com/oestadoma/geral/'
    ]

for link in links:
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='listaNoticiasMateria editorias-item__listaItem')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href'] 
        print(href)
