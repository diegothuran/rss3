# coding: utf-8

import sys
sys.path.insert(0, '../../src')

import feedparser

GLOBAL_RANK = 148 
RANK_BRAZIL = 5
NAME = 'g1.globo.com'

def get_urls():
    try:
        urls = [] 
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
    
        future_calls = [feedparser.parse(rss_url) for rss_url in hit_list]

        entries = []
        for feed in future_calls:
            entries.extend(feed["items"])

        for entrie in entries:

            ref_link = entrie['link']
            urls.append(ref_link)
        
        return urls
    except:
        raise Exception('Exception in globo')
