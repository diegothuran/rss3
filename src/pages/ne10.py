# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 17110
RANK_BRAZIL = 548 


def get_urls():
    try:
        urls = [] 
        for i in range(1,10):
            link = 'https://ne10.uol.com.br/radar/buscar/page:' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('li', class_='listagemDeNoticia-item')
            for noticia in noticias:
#                 print(noticia.find_all('a', href=True)[0]['href'])
                urls.append(noticia.find_all('a', href=True)[0]['href'])
        
        return urls
    except:
        raise Exception('Exception in ne10')

