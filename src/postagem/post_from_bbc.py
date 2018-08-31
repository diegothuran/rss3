import sys

sys.path.insert(0, '../../src')

import feedparser
import pandas as pd

from postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio
from postagem.lexical_analyzer import lexical
from postagem.site_wordpress import post_news
from Model.News import News
from Database.new_database import save_news, check_news

from newsplease import NewsPlease
from bs4 import BeautifulSoup
import requests

import datetime


start_url = 'https://www.bbc.com/portuguese/topics/75612fa6-147c-4a43-97fa-fcf70d9cced3'
search_div = 'eagle'

req = requests.get(start_url)
bs = BeautifulSoup(req.text)

itens = bs.find('div', class_='eagle').find_all('a', class_='title-link')


for item in itens:
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    article = NewsPlease.from_url('https://www.bbc.com' + item.get('href'))
    row['titulos'].append(article.title)
    row['noticia'].append(article.text)
    row['links'].append(article.url)
    row['abstract'].append(article.text)
    row['date'].append(article.date_publish)
    path_image = article.image_url
    if path_image == '' or path_image == None:
        row['image'].append(0)
    else:
        row['image'].append(download_and_move_image(article.image_url))
    news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
    try:
        print(row['titulos'])
        news_in_db = check_news(news)
        print('news_in_db: ' + str(news_in_db))
        if(not news_in_db):
            row = pd.DataFrame(row)
            df, categories = lexical(row)
            # DB categories
            if(categories != [set()]):
                news.set_categories(categories)
                save_news(news)
                post_news(df)
    except:
        print('Empty News')