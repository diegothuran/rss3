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

import util_seguranca


hit_list = [ 
    'http://g1.globo.com/dynamo/ac/acre/rss2.xml',
    'http://g1.globo.com/dynamo/al/alagoas/rss2.xml',
    'http://g1.globo.com/dynamo/ap/amapa/rss2.xml',
    'http://g1.globo.com/dynamo/am/amazonas/rss2.xml',
    'http://g1.globo.com/dynamo/bahia/rss2.xml',
    'http://g1.globo.com/dynamo/ceara/rss2.xml',
    'http://g1.globo.com/dynamo/distrito-federal/rss2.xml',
    'http://g1.globo.com/dynamo/espirito-santo/rss2.xml',
    'http://g1.globo.com/dynamo/goias/rss2.xml',
    'http://g1.globo.com/dynamo/ma/maranhao/rss2.xml',
    'http://g1.globo.com/dynamo/mato-grosso/rss2.xml',
    'http://g1.globo.com/dynamo/mato-grosso-do-sul/rss2.xml',
    'http://g1.globo.com/dynamo/minas-gerais/rss2.xml',
    'http://g1.globo.com/dynamo/mg/centro-oeste/rss2.xml',
    'http://g1.globo.com/dynamo/mg/grande-minas/rss2.xml',
    'http://g1.globo.com/dynamo/mg/sul-de-minas/rss2.xml',
    'http://g1.globo.com/dynamo/minas-gerais/triangulo-mineiro/rss2.xml',
    'http://g1.globo.com/dynamo/mg/vales-mg/rss2.xml',
    'http://g1.globo.com/dynamo/mg/zona-da-mata/rss2.xml',
    'http://g1.globo.com/dynamo/pa/para/rss2.xml',
    'http://g1.globo.com/dynamo/pb/paraiba/rss2.xml',
    'http://g1.globo.com/dynamo/pr/parana/rss2.xml',
    'http://g1.globo.com/dynamo/pr/campos-gerais-sul/rss2.xml',
    'http://g1.globo.com/dynamo/pr/oeste-sudoeste/rss2.xml',
    'http://g1.globo.com/dynamo/pr/norte-noroeste/rss2.xml',
    'http://g1.globo.com/dynamo/pernambuco/rss2.xml',
    'http://g1.globo.com/dynamo/pe/caruaru-regiao/rss2.xml',
    'http://g1.globo.com/dynamo/pe/petrolina-regiao/rss2.xml',
    'http://g1.globo.com/dynamo/rio-de-janeiro/rss2.xml',
    'http://g1.globo.com/dynamo/rj/regiao-serrana/rss2.xml',
    'http://g1.globo.com/dynamo/rj/regiao-dos-lagos/rss2.xml',
    'http://g1.globo.com/dynamo/rj/norte-fluminense/rss2.xml',
    'http://g1.globo.com/dynamo/rj/sul-do-rio-costa-verde/rss2.xml',
    'http://g1.globo.com/dynamo/rn/rio-grande-do-norte/rss2.xml',
    'http://g1.globo.com/dynamo/rs/rio-grande-do-sul/rss2.xml',
    'http://g1.globo.com/dynamo/ro/rondonia/rss2.xml',
    'http://g1.globo.com/dynamo/rr/roraima/rss2.xml',
    'http://g1.globo.com/dynamo/sc/santa-catarina/rss2.xml',
    'http://g1.globo.com/dynamo/sao-paulo/rss2.xml',
    'http://g1.globo.com/dynamo/sp/bauru-marilia/rss2.xml',
    'http://g1.globo.com/dynamo/sp/campinas-regiao/rss2.xml',
    'http://g1.globo.com/dynamo/sao-paulo/itapetininga-regiao/rss2.xml',
    'http://g1.globo.com/dynamo/sp/mogi-das-cruzes-suzano/rss2.xml',
    'http://g1.globo.com/dynamo/sp/piracicaba-regiao/rss2.xml',
    'http://g1.globo.com/dynamo/sp/presidente-prudente-regiao/rss2.xml',
    'http://g1.globo.com/dynamo/sp/ribeirao-preto-franca/rss2.xml',
    'http://g1.globo.com/dynamo/sao-paulo/sao-jose-do-rio-preto-aracatuba/rss2.xml',
    'http://g1.globo.com/dynamo/sp/santos-regiao/rss2.xml',
    'http://g1.globo.com/dynamo/sp/sao-carlos-regiao/rss2.xml',
    'http://g1.globo.com/dynamo/sao-paulo/sorocaba-jundiai/rss2.xml',
    'http://g1.globo.com/dynamo/sp/vale-do-paraiba-regiao/rss2.xml',
    'http://g1.globo.com/dynamo/se/sergipe/rss2.xml',
    'http://g1.globo.com/dynamo/to/tocantins/rss2.xml',
    'http://g1.globo.com/dynamo/vc-no-g1/rss2.xml'
    ]

while True:
    future_calls = [feedparser.parse(rss_url) for rss_url in hit_list]


    # In[3]:
    entries = []
    for feed in future_calls:
        entries.extend(feed["items"])


    i = 0
    news_from_globo = False
    for entrie in entries:
        i+=1
        print('\n Index: ' + str(i))
        ref_link = entrie['link']
        # get info from the ref_link and perform both post and db_save operations
        util_seguranca.news_from_link(ref_link, news_from_globo)

    # ref_link = 'https://www.torcedores.com/noticias/2018/09/galvao-expulsao-dede-cbf'
    # # get info from the ref_link and perform both post and db_save operations
    # util_midia.social_news_from_link(ref_link)




