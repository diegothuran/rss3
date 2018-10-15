# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

    
for i in range(1,10):
    if(i == 1):
        link = 'http://www.bastidoresdopoder.com.br/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='box-post-content')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='slide slide-1')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='slide slide-2')
        noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='slide slide-3')
    else:
        link = 'http://www.bastidoresdopoder.com.br/page/' + str(i)
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='box-post-content')
    
    for noticia in noticias:
        print(noticia.find_all('a', href=True)[0]['href'])
