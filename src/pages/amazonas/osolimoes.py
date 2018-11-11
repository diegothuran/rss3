# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 8474058
RANK_BRAZIL = None 
NAME = 'osolimoes'

def get_urls():
    try:
        urls = [] 
        root = 'http://osolimoes.com.br'
        for i in range(1, 10):
            if(i == 1):
                link = 'http://osolimoes.com.br/ver_noticias.html'
            else:
                link = 'http://osolimoes.com.br/ver_noticias.html?page=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='panel-content main-article-list')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in osolimoes')
