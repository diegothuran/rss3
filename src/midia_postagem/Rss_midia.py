# coding: utf-8

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


hit_list = [
    'http://braziljournal.com/rss',
    'http://jovempan.uol.com.br/feed',
    'http://www.huffpostbrasil.com/rss/index.xml',
    'http://www.jb.com.br/noticias/rss.xml',
    'http://www.jornaisvirtuais.com.br/feed/',
    'http://aosfatos.org/noticias/feed/',
    'https://apublica.org/feed/',
    'http://br.sputniknews.com/export/rss2/archive/index.xml',
    'https://catracalivre.com.br/feed/',
    'https://www.metropoles.com/feed',
    'http://www.opopular.com.br/cmlink/o-popular-%C3%BAltimas-1.272904',
    'http://altamiroborges.blogspot.com/feeds/posts/default',
    'http://avozeavezdajuventude.blogspot.com/feeds/posts/default',
    'http://blogdoprimo.com.br/feed/',
    'http://blogdoriella.com.br/feed/',
    'http://blogdoskarlack.com/feed/',
    'http://www.jornalcash.com.br/?feed=rss2',
    'http://blogmarcosfrahm.com/feed/',
    'http://congressoemfoco.uol.com.br/feed/',
    'http://elielbezerra.blogspot.com/feeds/posts/default',
    'http://osamigosdopresidentelula.blogspot.com/feeds/posts/default',
    'http://outraspalavras.net/feed/',
    'http://outroladodanoticia.com.br/feed/',
    'http://polibiobraga.blogspot.com/feeds/posts/default',
    'http://poncheverde.blogspot.com/feeds/posts/default',
    'http://previdi.blogspot.com/feeds/posts/default',
    'http://sembalela.com/feed/',
    'http://www.blogdafloresta.com.br/feed/',
    'http://www.blogdoataide.com.br/feed/',
    'http://www.blogdoluciosorge.com.br/feed/',
    'http://www.diariodocentrodomundo.com.br/feed/',
    'http://www.fabiocampana.com.br/feed/',
    'http://www.imprensaviva.com/feeds/posts/default',
    'http://www.jaderbarbalho.com/v3/index.php/feed/',
    'http://www.ma10.com.br/minard/feed/',
    'https://www.ocafezinho.com/feed/',
    'http://www.ocombatente.com/feed/',
    'http://www.politicanarede.com/feeds/posts/default',
    'http://www.redebrasilatual.com.br/ultimas-noticias/atom.xml',
    'http://www.saibamais.jor.br/feed/',
    'http://www.tijolaco.com.br/blog/feed/',
    'http://www.vermelho.org.br/xml/rss_noticias.xml',
    'https://blogdoneylopes.wordpress.com/feed/',
    'http://br.sputniknews.com/export/rss2/archive/index.xml',
    'https://osdivergentes.com.br/feed/',
    'https://www.balaiodokotscho.com.br/feed/',
    'https://www.brasildefato.com.br/rss2.xml',
    'https://www.ceticismopolitico.org/feed/',
    'https://www.domingoscosta.com.br/feed/',
    'https://www.oantagonista.com/feed/',
    'https://jornalivre.com/feed/',
    'http://marcossilverio.blogspot.com/feeds/posts/default',
    'http://mauriciostycer.blogosfera.uol.com.br/feed/',
    'http://www.otvfoco.com.br/feed/',
    'http://www.telesintese.com.br/feed/',
    'http://www.vcfaz.tv/rssnews.php?f=17',
    'http://feed.observatoriodatelevisao.bol.uol.com.br/feed',
    'http://comunicadores.info/feed/',
    'http://portaldapropaganda.com.br/noticias/feed/',
    'http://www.administradores.com.br/rss/noticias/',
    'http://www.bluebus.com.br/feed/',
    'http://www.inteligemcia.com.br/feed/',
    'http://www.papelpop.com/feed/',
    'http://www.updateordie.com/feed/',
    'http://www.mundodomarketing.com.br/feed/rss.xml',
    'https://www.promoview.com.br/feed.rss',
    'http://feeds.feedburner.com/gospelprime',
    'http://justificando.cartacapital.com.br/feed/',
    'https://www.comunique-se.com.br/feed/',
    'https://www.torcedores.com/comments/feed',
    'http://www.portalmidiaesporte.com/feeds/posts/default',
    'http://www.esporteemidia.com/feeds/posts/default',
    'https://blogdopaulinho.com.br/feed/',
    'http://www.mktesportivo.com/feed/',
    'http://www.mtesporte.com.br/rss.php',
    'http://lulacerda.ig.com.br/feed/',
    'https://www.tecmundo.com.br/busca?q=feed',
    'https://www12.senado.leg.br/noticias/feed/todasnoticias/RSS',
    'https://www.ancine.gov.br/pt-br/rss.xml',
    'https://gife.org.br/feed/',
    'http://www.pt.org.br/feed/',
    'http://servicios.lanacion.com.ar/herramientas/rss/origen=2'
    ]

future_calls = [feedparser.parse(rss_url) for rss_url in hit_list]


# In[3]:
entries = []
for feed in future_calls:
    entries.extend(feed["items"])


resultados = pd.DataFrame({'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []})


def format_date(raw_date):
    formated_date = datetime.datetime.strptime(raw_date, '%d/%m/%Y %Hh%M%S').strftime("%Y-%m-%d %H:%M:%S")
    return formated_date

i = 0
for entrie in entries:
    i+=1
    row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
    domain = extract_domain(entrie['link'])
    print('\n Index: ' + str(i))
    print(domain)
    path_image = ""
    ref_link = entrie['link']
    
    article = NewsPlease.from_url(ref_link)
    # Data returned by the NewsPlease
    row['titulos'].append(article.title)
    row['noticia'].append(article.text)
    row['links'].append(article.url)
    row['abstract'].append(article.text)
    formated_date = str(article.date_publish)
    row['date'].append(formated_date)
    
    path_image = article.image_url
    if path_image == '' or path_image == None:
        row['image'].append(0)
    else:
        row['image'].append(download_and_move_image(article.image_url))
  
    news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
   
    try:
        print(row['titulos'])
        news_in_db = midia_table.check_news(news)
        print('news_in_db: ' + str(news_in_db))
        if(not news_in_db):
            row = pd.DataFrame(row)
            df, categories = midia_lexical.lexical_corpus_and_title(row)
            # DB categories
            if(categories != [set()]):
                news.set_categories(categories)
                midia_table.save_news(news)
                midia_post.post_news(df)
    except:
        print('Empty News')


