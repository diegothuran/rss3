# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 2031641
RANK_BRAZIL = None
NAME = 'correiodopovo_al'


def get_urls():
    try:
        urls = [] 
        root = 'http://www.correiodopovo-al.com.br'
        
        for i in range(1, 10):
            if(i == 1):
                link = 'http://www.correiodopovo-al.com.br/index.php/noticias'
            else:
                link = 'http://www.correiodopovo-al.com.br/index.php/noticias/listar?pagina=' + str(i)
            req = requests.get(link)
            
            noticias = BeautifulSoup(req.text, "html.parser").find_all('a', class_='row', href=True)
            for noticia in noticias:
                href = noticia['href']
                full_link = root + href 
#                 print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in correiodopovo')
