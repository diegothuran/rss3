
# coding: utf-8

# In[1]:


import sys
sys.path.insert(0, '../../src')
import feedparser
import pandas as pd

import urllib

from postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio
from lexical_analyzer_package import midia_lexical
from midia_postagem import midia_post
from Model.News import News
from Database import midia_table

from newsplease import NewsPlease
from bs4 import BeautifulSoup
import requests
import util_midia
import datetime


# In[2]:


link = 'http://www.ebc.com.br'


# In[3]:


req = requests.get(link)


# In[4]:


noticias = BeautifulSoup(req.text, "html.parser").find_all('div', class_='cmpGeneric isoGrid-item col-lg-4 col-md-4 col-sm-12 col-xs-12')


# In[5]:


for noticia in noticias:
    print(noticia.find_all('a', href=True)[0]['href'])
    util_midia.social_news_from_link(noticia.find_all('a', href=True)[0]['href'])