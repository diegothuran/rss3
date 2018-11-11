# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1394846
RANK_BRAZIL = 70062 
NAME = 'oriobranco'

def get_urls():
    try:
        urls = [] 
        root = 'http://www.oriobranco.net/'
        for i in range(1,10):
            if(i == 1):
                link = 'http://www.oriobranco.net/policial'
            else:
                link = 'http://www.oriobranco.net/policial/pagina/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='destaque-thumb foto clearfix')
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in oriobranco_policial')

