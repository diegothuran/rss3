# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 3451841
RANK_BRAZIL = 64001 
NAME = 'jornalnovafronteira'


def get_urls():
    try:
        urls = [] 
        for i in range(1, 10):
            if(i == 1):
                link = 'http://jornalnovafronteira.com.br/c/canais/'
            else:
                link = 'http://jornalnovafronteira.com.br/c/canais/page/' + str(i)
                
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', id='detalhes')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in jornalnovafronteira')

