# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1508245
RANK_BRAZIL = 82562
NAME = 'portaldapropaganda.com.br'

def get_urls():
    try:
        urls = [] 
        link = 'http://www.portaldapropaganda.com.br/noticias/'
        req = requests.get(link)
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in portaldapropaganda')
    
