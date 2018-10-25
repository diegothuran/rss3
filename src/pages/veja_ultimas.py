# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests


def get_urls():
    try:
        urls = [] 
        
        link = 'https://veja.abril.com.br/ultimas-noticias/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='list-item')
        for noticia in noticias:
#             print(noticia.find_all('a', href=True)[0]['href'])
            urls.append(noticia.find_all('a', href=True)[0]['href'])
        
        return urls
    except:
        raise Exception('Exception in veja_ultimas')
