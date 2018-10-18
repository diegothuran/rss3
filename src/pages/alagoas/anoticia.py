# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests


links = [
        'http://www.anoticia.online/category/politica/',
        'http://www.anoticia.online/category/brasil/',
        'http://www.anoticia.online/category/mundo/',
        'http://www.anoticia.online/category/policia/',
        'http://www.anoticia.online/category/economia/'
        ]


for link in links:
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='bold xt-post-title')
    for noticia in noticias:    
        href = noticia.find_all('a', href=True)[0]['href']
#         full_link = root + href 
        print(href)
        
