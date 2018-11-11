# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 4267112
RANK_BRAZIL = None
NAME = 'oecojornal'


def get_urls():
    try:
        urls = [] 
        link = 'http://oecojornal.com.br/'
        req = requests.get(link)
        
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href']
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in oecojornal')
