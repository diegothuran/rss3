# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 8504964
RANK_BRAZIL = None
NAME = 'folharegionalbahia.com.br'


def get_urls():
    try:
        urls = [] 
        link = 'https://folharegionalbahia.com.br/'
        req = requests.get(link)
        
        noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='entry-title td-module-title')
        for noticia in noticias:
            href = noticia.find_all('a', href=True)[0]['href'] 
#             print(href)
            urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in folharegionalbahia')
