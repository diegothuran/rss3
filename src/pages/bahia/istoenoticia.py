# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

# root = 'http://istoenoticia.com/'
link = 'http://istoenoticia.com/'
req = requests.get(link)
noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='feature-title')
noticias += BeautifulSoup(req.text, "html.parser").find_all('h4', class_='entry-title')
noticias += BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title')


for noticia in noticias:
    href = noticia.find_all('a', href=True)[0]['href']
#     full_link = root + href 
    print(href)
