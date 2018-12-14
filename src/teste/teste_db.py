#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../src')
from Model import News
from Database import connection, relevancia_site_table
import datetime
from dateutil import parser
import postagem.Util as Util
from Model.Relevancia_Site import Relevancia_Site 
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from Util import util




# site = 'oestadoacre'
# estrutura tupla = (id, site, relevancia)
# tupla = relevancia_site_table.select(site)


# def plot_bar_timeseries(valores, dates):
#     # this is for plotting purpose
# #     index = np.arange(len(valores))
#     index = []
#     for date in dates:
# #         str_date = date.strftime("%Y-%m-%d")
#         str_date = date.strftime("%d-%m-%Y")
#         index.append(str_date)
#     plt.bar(index, valores)
#     plt.xlabel('Data', fontweight='bold')
#     plt.ylabel('Número de notícias', fontweight='bold')
#     plt.xticks(rotation=30)
#     plt.title('Timeline das notícias')
# #     plt.xlabel('Genre', fontsize=5)
# #     plt.ylabel('No of Movies', fontsize=5)
# #     plt.xticks(index, valores, fontsize=5, rotation=30)
# #     plt.title('Market Share for Each Genre 1995-2017')
#     plt.show()
#       
# # dates = [datetime.date(2018, 11, 1), datetime.date(2018, 11, 2), datetime.date(2018, 11, 3), datetime.date(2018, 11, 4)]
#            
# dates = [datetime.date(2018, 11, 1), datetime.date(2018, 11, 2), datetime.date(2018, 11, 3), datetime.date(2018, 11, 4), 
#          datetime.date(2018, 11, 5), datetime.date(2018, 11, 6), datetime.date(2018, 11, 7), datetime.date(2018, 11, 8),
#          datetime.date(2018, 11, 9), datetime.date(2018, 11, 10), datetime.date(2018, 11, 11), datetime.date(2018, 11, 12), datetime.date(2018, 11, 13)]
#   
# valores = []
# for date in dates:
#     valores.append(relevancia_site_table.select_form_date(date))
#   
# print(valores)
# plot_bar_timeseries(valores, dates)
 
# data_inicial = datetime.date(2018, 11, 1) 
# data_final = datetime.date(2018, 11, 4)
# relevancia_site_table.get_interval(data_inicial, data_final)

site = 'www.valor.com.br'
# relevancia_site_table.select_site_in_link(site)
relevancia_site_table.update_site(site)
 
# relevancia_site_table.select_site(site)
# 
# # categories_db = relevancia_site_table.select_site_pd(site)
# # n_news = float(len(categories_db)) 
# # print(categories_db)
# 
# 
# # THEME_CATEGORIES = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes']
# 
# THEME_CATEGORIES = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'sérgio moro', 'hamilton mourão',
#                      'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina',
#                      'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 
#                      'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 
#                      'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 
#                      'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno']
# 
# 
# INDEX_CATEGORIES = {
# #     'categoria': '',
#                     'bolsonaro' : 0,
#                     'onyx lorenzoni' : 0, 
#                     'paulo guedes' : 0, 
#                     'augusto heleno' : 0, 
#                     'marcos pontes' : 0, 
#                     'sérgio moro' : 0,
#                     'hamilton mourão' : 0,
#                     'joaquim levy' : 0,
#                     'mansueto almeida' : 0,
#                     'fernando azevedo e silva' : 0,
#                     'ernesto araújo' : 0, 
#                     'roberto campos neto' : 0,
#                     'tereza cristina' : 0,
#                     'andré luiz de almeida mendonça' : 0,
#                     'carlos von doellinger' : 0,
#                     'érika marena' : 0,
#                     'luiz mandetta' : 0,
#                     'maurício valeixo' : 0,
#                     'pedro guimarães' : 0,
#                     'ricardo vélez rodríguez' : 0,
#                     'roberto castello branco' : 0,
#                     'rubem novaes' : 0,
#                     'wagner rosário' : 0,
#                     'bento costa lima leite de albuquerque junior' : 0, 
#                     'marcelo álvaro antônio' : 0, 
#                     'osmar terra' : 0, 
#                     'gustavo henrique rigodanzo canuto' : 0, 
#                     'tarcísio gomes de freitas' : 0, 
#                     'carlos alberto dos santos cruz' : 0, 
#                     'gustavo bebianno' : 0,
# 
#                     'jungmann' : 0, 
#                     'haddad' : 0, 
#                     'ac' : 0,
#                     'al' : 0,
#                     'ap' : 0,
#                     'am' : 0,
#                     'ba' : 0,
#                     'ce' : 0,
#                     'df' : 0,
#                     'es' : 0,
#                     'go' : 0,
#                     'ma' : 0,
#                     'mt' : 0,
#                     'ms' : 0,
#                     'mg' : 0,
#                     'pa' : 0,
#                     'pb' : 0,
#                     'pr' : 0,
#                     'pe' : 0,
#                     'pi' : 0,
#                     'rj' : 0,
#                     'rn' : 0,
#                     'rs' : 0,
#                     'ro' : 0,
#                     'rr' : 0,
#                     'sc' : 0,
#                     'sp' : 0,
#                     'se' : 0,
#                     'to' : 0
#                     }
# 
# retorno = []
# for theme in THEME_CATEGORIES:
#     row = INDEX_CATEGORIES.copy()
# #     row['categoria'] = theme
#     for categories_per_row in categories_db:
#         if(theme in categories_per_row):
#             if(',' in categories_per_row):
#                 categories = categories_per_row.split(', ')
#                 for category in categories:
#                     row[category] += 1
#             else: # only one category in the table
#                 row[categories_per_row] += 1
#     retorno.append(row)
# 
# print('retorno')
# print(len(retorno))
# df = pd.DataFrame(retorno, index=THEME_CATEGORIES)
# # print(df.loc['bolsonaro'])
# for i in range(len(df)):
#     print(i)
# #     print(df.iloc[i].name)
#     print(df.iloc[i].values)
#     valores = df.iloc[i].values
# #     soma = np.sum(valores)
# #     print(soma)
#     percentagem = None
#     percentagem =  valores/n_news
#     print(percentagem)
# print(df)
# 
# # a = list(retorno[0].values())
# # b = a[1:]
# 
# # print(np.cov(b))
# 
# # print('\n COOR MATRIX')
# # # df['A'].corr(df['B'])
# # # coor_matrix = df.corr()
# # coor_matrix = df.corr()
# # 
# # print(coor_matrix['bolsonaro'])
# # print(len(coor_matrix['bolsonaro']))

