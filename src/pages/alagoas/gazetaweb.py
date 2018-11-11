# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

#based on the rank of globo
GLOBAL_RANK = 147 
RANK_BRAZIL = 5
NAME = 'gazetaweb'

def get_urls():
    try:
        urls = [] 
        
        for idx in range(1,9):
            link = 'http://gazetaweb.globo.com/portal/editoria.php?c=' + str(idx)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('a', class_='com-foto', href=True)
            for noticia in noticias:
                href = noticia['href']
#                 print(href)
                urls.append(href)
        
        return urls
    except:
        raise Exception('Exception in gazetaweb')
