
# coding: utf-8

import urllib
from bs4 import BeautifulSoup
import requests
from newsplease import NewsPlease

import datetime
import pandas as pd

from src.postagem.Util import extract_domain, download_and_move_image, get_noticia_comercio
from src.postagem.lexical_analyzer import lexical, lexical_soup_globo
from src.postagem.site_wordpress import post_news
from src.Model.News import News
from src.Database.new_database import save_news, check_news
import time

def format_date(raw_date):
    formated_date = datetime.datetime.strptime(raw_date, ' %d/%m/%Y %Hh%M ').strftime("%Y-%m-%d %H:%M:%S")
    return formated_date

# Centro-Oeste
# link = 'https://g1.globo.com/df/distrito-federal/eleicoes/2018/'
# link = 'https://g1.globo.com/go/goias/eleicoes/2018/'
# link = 'https://g1.globo.com/mt/mato-grosso/eleicoes/2018/'
# link = 'https://g1.globo.com/ms/mato-grosso-do-sul/eleicoes/2018/'

# Nordeste
# link = 'https://g1.globo.com/al/alagoas/eleicoes/2018/'
# link = 'https://g1.globo.com/ba/bahia/eleicoes/2018/'
# link = 'https://g1.globo.com/ce/ceara/eleicoes/2018/'
# link = 'https://g1.globo.com/ma/maranhao/eleicoes/2018/'
# link = 'https://g1.globo.com/pb/paraiba/eleicoes/2018/'
# link = 'https://g1.globo.com/pe/pernambuco/eleicoes/2018/'
# link = 'https://g1.globo.com/pi/piaui/eleicoes/2018/'
# link = 'https://g1.globo.com/rn/rio-grande-do-norte/eleicoes/2018/'
# link = 'https://g1.globo.com/se/sergipe/eleicoes/2018/'

# Norte
# link = 'https://g1.globo.com/ac/acre/eleicoes/2018/'
# link = 'https://g1.globo.com/ap/amapa/eleicoes/2018/'
# link = 'https://g1.globo.com/am/amazonas/eleicoes/2018/'
# link = 'https://g1.globo.com/pa/para/eleicoes/2018/'
# link = 'https://g1.globo.com/ro/rondonia/eleicoes/2018/'
# link = 'https://g1.globo.com/rr/roraima/eleicoes/2018/'
# link = 'https://g1.globo.com/to/tocantins/eleicoes/2018/'

# Sudeste
# link = 'https://g1.globo.com/es/espirito-santo/eleicoes/2018/'
# link = 'https://g1.globo.com/mg/minas-gerais/eleicoes/2018/'
# link = 'https://g1.globo.com/rj/rio-de-janeiro/eleicoes/2018/'
# link = 'https://g1.globo.com/sp/sao-paulo/eleicoes/2018/'

# Sul
# link = 'https://g1.globo.com/pr/parana/eleicoes/2018/'
# link = 'https://g1.globo.com/rs/rio-grande-do-sul/eleicoes/2018/'
# link = 'https://g1.globo.com/sc/santa-catarina/eleicoes/2018/'



links = ['https://g1.globo.com/df/distrito-federal/eleicoes/2018/',
         'https://g1.globo.com/go/goias/eleicoes/2018/',
         'https://g1.globo.com/mt/mato-grosso/eleicoes/2018/',
         'https://g1.globo.com/ms/mato-grosso-do-sul/eleicoes/2018/',
         'https://g1.globo.com/al/alagoas/eleicoes/2018/',
         'https://g1.globo.com/ba/bahia/eleicoes/2018/',
         'https://g1.globo.com/ce/ceara/eleicoes/2018/',
         'https://g1.globo.com/ma/maranhao/eleicoes/2018/',
         'https://g1.globo.com/pb/paraiba/eleicoes/2018/',
         'https://g1.globo.com/pe/pernambuco/eleicoes/2018/',
         'https://g1.globo.com/pi/piaui/eleicoes/2018/',
         'https://g1.globo.com/rn/rio-grande-do-norte/eleicoes/2018/',
         'https://g1.globo.com/se/sergipe/eleicoes/2018/',
         'https://g1.globo.com/ac/acre/eleicoes/2018/',
         'https://g1.globo.com/ap/amapa/eleicoes/2018/',
         'https://g1.globo.com/am/amazonas/eleicoes/2018/',
         'https://g1.globo.com/pa/para/eleicoes/2018/',
         'https://g1.globo.com/ro/rondonia/eleicoes/2018/',
         'https://g1.globo.com/rr/roraima/eleicoes/2018/',
         'https://g1.globo.com/to/tocantins/eleicoes/2018/',
         'https://g1.globo.com/es/espirito-santo/eleicoes/2018/',
         'https://g1.globo.com/mg/minas-gerais/eleicoes/2018/',
         'https://g1.globo.com/rj/rio-de-janeiro/eleicoes/2018/',
         'https://g1.globo.com/sp/sao-paulo/eleicoes/2018/',
         'https://g1.globo.com/pr/parana/eleicoes/2018/',
         'https://g1.globo.com/rs/rio-grande-do-sul/eleicoes/2018/',
         'https://g1.globo.com/sc/santa-catarina/eleicoes/2018/'
    ]

for link in links:
    print('url_globo: ' + str(link))
    page = urllib.request.urlopen(link)
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')
    
    news = soup.find_all('div', class_='feed-post bstn-item-shape type-materia')
    for new in news:
        row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
        
        internal_link = new.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover', href=True)
        ref = internal_link[0]['href']
        article = NewsPlease.from_url(ref)
    #     abstract = article.description
    #     print(abstract)
        
        # Data returned by the NewsPlease
        titulo = article.title
        noticia = article.text
        image_url = None
        image_url = article.image_url
        news_url = article.url
        
        # we need to get the date from the original url, the date returned by the NewsPlease is wrong
        page_time = urllib.request.urlopen(news_url)
        soup_date = BeautifulSoup(page_time, 'html.parser')
        time_tag = soup_date.find_all('time', attrs={'itemprop': 'datePublished'})
        public_date = time_tag[0].text 
        formated_date = format_date(public_date)
        
        row['titulos'].append(titulo)
        row['links'].append(news_url)
        row['date'].append(formated_date)
        row['noticia'].append(noticia)
        row['abstract'].append(noticia)
        if(image_url is not None):
            path_image = image_url
            row['image'].append(download_and_move_image(path_image))
        else:
            row['image'].append(0)
            
        news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
    
        try:
            print(row['titulos'])
            news_in_db = check_news(news)
            print('news_in_db: ' + str(news_in_db))
            if(not news_in_db):
                row = pd.DataFrame(row)
                df, categories = lexical_soup_globo(row)
                # DB categories
                news.set_categories(categories)
                save_news(news)
                post_news(df)
        except:
            print('Empty News')
    
    print('\n --- SLEEP --- ')
    time.sleep(60)