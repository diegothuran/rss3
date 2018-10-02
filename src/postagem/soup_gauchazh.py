import sys
sys.path.insert(0, '../../src')

import pandas as pd
from bs4 import BeautifulSoup
import requests

from postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio
from postagem.lexical_analyzer import lexical, lexical_soup_globo
from postagem.site_wordpress import post_news
from newsplease import NewsPlease
from Model.News import News
from Database.new_database import save_news, check_news


link = 'https://gauchazh.clicrbs.com.br/politica/eleicoes/ultimas-noticias/'
req = requests.get(link)
bs = BeautifulSoup(req.text, "html.parser")
materias = bs.find('section', class_='section-latest-page').find_all('div', class_='card')

for materia in materias:
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    article = NewsPlease.from_url('https://gauchazh.clicrbs.com.br/' + materia.find('a', href=True)['href'])
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
        if (not news_in_db):
            row = pd.DataFrame(row)
            df, categories = lexical(row)
            # DB categories
            if (categories != [set()]):
                news.set_categories(categories)
                save_news(news)
                post_news(df)
    except:
        print('Empty News')
