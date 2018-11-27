# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

#pegou o rank do clicrbs
GLOBAL_RANK = 4526
RANK_BRAZIL = 148    
NAME = 'clicrbs'

def get_urls():
    try:
        urls = [] 
        
        for i in range(1,5):
            if(i == 1):
                link = 'http://anoticia.clicrbs.com.br/sc/ultimas-noticias/'
            else:
                link = 'http://anoticia.clicrbs.com.br/sc/ultimas-noticias/?pagina=' + str(i)
            req = requests.get(link)
            noticias = BeautifulSoup(req.text, "html.parser").find_all('h2', class_='materia-manchete')
            
            for noticia in noticias:
                href = noticia.find_all('a', href=True)[0]['href']
                urls.append(href)
                
        return urls
    except:
        raise Exception('Exception in anoticia_clicrbs')
