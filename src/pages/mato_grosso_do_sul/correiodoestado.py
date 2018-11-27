# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

GLOBAL_RANK = 73123
RANK_BRAZIL = 2764   
NAME = 'correiodoestado'

def get_urls():
    try:
        urls = [] 
        
        for i in range(1, 5):
            if(i == 1):
                link = 'https://www.correiodoestado.com.br/ultimas-noticias/'
            else:
                link = 'https://www.correiodoestado.com.br/ultimas-noticias/p/' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='noticiaLink')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in correiodoestado')
