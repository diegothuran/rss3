# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

for i in range(1,10):
    if(i == 1):
        link = 'http://www.justificando.com/categoria/noticias/'
    else:
        link = 'http://www.justificando.com/categoria/noticias/page/2/'
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('h4', class_='entry-title entry-title-left')
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        print(href)
