# coding: utf-8

import sys
sys.path.insert(0, '../../src')
from bs4 import BeautifulSoup
import requests

root = 'http://www.novoeste.com/'
for i in range(1, 10):
    if(i == 1):
        link = 'http://www.novoeste.com/index.php?page=destaque'
    else:
        link = 'http://www.novoeste.com/index.php?page=destaque&pg=' + str(i)
        
    req = requests.get(link)
    noticias = BeautifulSoup(req.text, "html.parser").find_all('h1')
    
    for noticia in noticias:
        href = noticia.find_all('a', href=True)[0]['href']
        full_link = root + href
        print(full_link)