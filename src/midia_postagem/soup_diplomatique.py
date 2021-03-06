# deixei só as notícias mais recentes nesse site
#ficou muito complicado pegar o site completo de uma vez
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

import util_midia

link = 'https://diplomatique.org.br/'
req = requests.get(link)
bs = BeautifulSoup(req.text, "html.parser")
materias = bs.find_all('div', class_='owl-carousel')

for div in materias[1:]:
    try:
        page_link = div.find_all('a', href=True)[0]['href']
        
        util_midia.social_news_from_link(page_link)
        
#         article = NewsPlease.from_url(page_link)
#         print(article.title)
#         row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
#         if (article is not None):
#             row['titulos'].append(article.title)
#             row['noticia'].append(article.text)
#             row['links'].append(article.url)
#             row['abstract'].append(article.text)
#             row['date'].append(article.date_publish)
#             path_image = article.image_url
#             if path_image == '' or path_image == None:
#                 row['image'].append(0)
#             else:
#                 row['image'].append(download_and_move_image(article.image_url))
#             news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
#             try:
#                 print(row['titulos'])
#                 news_in_db = midia_table.check_news(news)
#                 print('news_in_db: ' + str(news_in_db))
#                 if (not news_in_db):
#                     row = pd.DataFrame(row)
#                     df, categories = midia_lexical.lexical_corpus_and_title(row)
#                     # DB categories
#                     if (categories != [set()]):
#                         news.set_categories(categories)
#                         midia_table.save_news(news)
#                         midia_post.post_news(df)
#             except:
#                 print('Empty News')
    except:
        pass
