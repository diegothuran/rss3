# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests
from pages.util.constantes import PAGE_LIMIT

GLOBAL_RANK = 8772
RANK_BRAZIL = 240 
NAME = 'agenciabrasil.ebc.com.br'

def get_urls():
    try:
        root = 'http://agenciabrasil.ebc.com.br'
        urls = []
        for i in range(PAGE_LIMIT):
            if(i == 0):
                link = 'http://agenciabrasil.ebc.com.br/ultimas'
            else:
                link = 'http://agenciabrasil.ebc.com.br/ultimas?page=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h3', class_='heading')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                full_link = root + href 
    #             print(full_link)
                urls.append(full_link)
        
        return urls
    except:
        raise Exception('Exception in agenciabrasil_ebc')