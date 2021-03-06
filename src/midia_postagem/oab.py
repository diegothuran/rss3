
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

import datetime
import util_midia


# In[2]:


link = 'https://www.oab.org.br/'


# In[3]:


link_site = 'https://www.oab.org.br/'


# In[4]:


req = requests.get(link)


# In[5]:


noticias = BeautifulSoup(req.text, "html.parser").find_all('article', class_='col6 coluna')


# In[6]:


for noticia in noticias:
    print(noticia.find_all('a', href=True)[0]['href'])
    ref_link = noticia.find_all('a', href=True)[0]['href']
    #print(link_site+ref_link)
    if (link_site not in ref_link):
        util_midia.social_news_from_link(link_site+ref_link)
        print(link_site+ref_link)
    else:
        util_midia.social_news_from_link(ref_link)
        print(ref_link)


# In[7]:


noticias[0]

