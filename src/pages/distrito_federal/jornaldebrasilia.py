# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 96868
RANK_BRAZIL = 3520 


def get_urls():
    try:
        urls = [] 
        for i in range(1, 10):
            if(i == 1):
                link = 'http://www.jornaldebrasilia.com.br/arquivos/'
                req = requests.get(link)
                noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='brasilia-highlights__item')
                noticias += BeautifulSoup(req.text, "html.parser").find_all('div', class_='highlight-block__item-details')
                
            else:
                link = 'http://www.jornaldebrasilia.com.br/arquivos/page/' + str(i)
                req = requests.get(link)
                noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='highlight-block__item-details')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornaldebrasilia')
