# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

def get_urls():
    try:
        urls = [] 
        root = 'http://diariodonordeste.verdesmares.com.br/'
        for i in range(1, 9):
            link = 'http://diariodonordeste.verdesmares.com.br/servicos/ultima-hora?page=' + str(i) +'#pagination'
            
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='c-teaser__text')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in diariodonordeste')
