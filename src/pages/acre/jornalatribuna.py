# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

from pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 2675408
RANK_BRAZIL = None
NAME = 'jornalatribuna'


def get_urls():
    try:
        urls = [] 
        categorias = ['2', '9', '16']
        for categoria in categorias:
            for i in range(1,PAGE_LIMIT):
                if(i == 1):
                    link = 'http://www.jornalatribuna.com.br/?cat=' + categoria
                else:
                    link = 'http://www.jornalatribuna.com.br/?cat='+ categoria +'&paged=' + str(i)
                req = requests.get(link)
                noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='entry-title')
                for noticia in noticias:
                    href = noticia.find_all('a', href=True)[0]['href']
#                     print(href)
                    urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornalatribuna')
