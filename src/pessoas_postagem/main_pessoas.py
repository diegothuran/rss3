# coding: utf-8

import sys
sys.path.insert(0, '../../src')


# import feedparser
from pessoas_postagem import util_pessoas

from pages import agenciabrasil_ebc, bastidoresdopoder, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo, \
diariodocentrodomundo_mundo, diariodonordeste, dinheirorural, exame, gazetadopovo, infomoney, istoedinheiro, jornalestadodeminas, \
jovempan, justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, terra_noticias, tnh1, tribunadosertao, veja_ultimas

""" List of pages """
pages = [agenciabrasil_ebc, bastidoresdopoder, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo, 
         diariodocentrodomundo_mundo, diariodonordeste, dinheirorural, exame, gazetadopovo, infomoney, istoedinheiro, jornalestadodeminas, 
         jovempan, justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, terra_noticias, tnh1, tribunadosertao, veja_ultimas]


for page in pages:
    try:
        urls = page.get_urls()
        news_from_globo = False
        for url in urls:
            print('\n' + url)
            util_pessoas.news_from_link(url, news_from_globo)
 
    except Exception as e:
        print(e)
        pass