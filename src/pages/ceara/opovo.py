# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests


links = [
        'https://www.opovo.com.br/noticias/politica/',
        'https://www.opovo.com.br/noticias/fortaleza/',
        'https://www.opovo.com.br/noticias/economia/',
        'https://www.opovo.com.br/noticias/brasil/',
        'https://www.opovo.com.br/noticias/ceara/',
        'https://www.opovo.com.br/noticias/mundo/'
    ]

for link in links:
    req = requests.get(link)
    ultags = BeautifulSoup(req.text, "html.parser").find_all('ul', class_='listagem listagem-noticias')    
    for ul in ultags:
        for li in ul.find_all('li'):
            href = li.find_all('a', href=True)[0]['href']
            print(href)
