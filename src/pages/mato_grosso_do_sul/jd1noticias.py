# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 1125849
RANK_BRAZIL = 31946    
NAME = 'jd1noticias'

def get_urls():
    try:
        urls = [] 
        
        for i in range(1, 5):
            link = 'http://www.jd1noticias.com/canal/ultimas-noticias/p/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('ul', class_='listNoticias listCanal')
            
            for lista in noticias:
                for noticia in lista:
                    try:
                        href = noticia.find_all('a', href=True)[0]['href']
                        urls.append(href)
                    except:
                        pass
        return urls
    except:
        raise Exception('Exception in jd1noticias')
