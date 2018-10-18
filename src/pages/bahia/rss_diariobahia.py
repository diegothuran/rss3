# coding: utf-8

import sys
sys.path.insert(0, '../../src')


import feedparser
import pandas as pd

import urllib

from postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio
from lexical_analyzer_package import midia_lexical
from midia_postagem import midia_post
from Model.Social_News import Social_News
from Database import midia_table

from newsplease import NewsPlease
from bs4 import BeautifulSoup
import requests

import datetime


hit_list = [ 
    'http://diariobahia.com.br/feed/'
    ]

future_calls = [feedparser.parse(rss_url) for rss_url in hit_list]


# In[3]:
entries = []
for feed in future_calls:
    entries.extend(feed["items"])

i = 0
news_from_globo = False
for entrie in entries:
    i+=1
    ref_link = entrie['link']
    print(ref_link)
    # get info from the ref_link and perform both post and db_save operations
#             util_seguranca.news_from_link(ref_link, news_from_globo)



