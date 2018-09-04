#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../../src')

from lexical_analyzer_package import base_lexical_analyzer

import nltk

# import pandas as pd
# import string 
# import numpy as np

# stemmer = nltk.stem.RSLPStemmer()
# stemmer.stem("copiar")

# categories related to the main theme: security in this case
WORDS = ['comércio', 
         'ecommerce', 'e-commerce', 'comércio eletrônico',
         'vendas', 
         'lojas', 
         'shopping', 
         'presente', 
         'dia dos pais', 
         'dia das mães', 
         'dia dos namorados', 
         'dia das crianças', 
         'dia dos professores', 
         'natal', 
         'páscoa', 
         'são joão', 
         'carnaval']

THEME_CATEGORIES = ['comércio', 
                     'ecommerce', 'ecommerce', 'ecommerce',
                     'vendas', 
                     'lojas', 
                     'shopping', 
                     'presente', 
                     'dia dos pais', 
                     'dia das mães', 
                     'dia dos namorados', 
                     'dia das crianças', 
                     'dia dos professores', 
                     'natal', 
                     'páscoa', 
                     'são joão', 
                     'carnaval']

def lexical(df):
    df, categories = base_lexical_analyzer.get_categories_corpus(df, WORDS, THEME_CATEGORIES)
    return df, categories
 
def lexical_corpus_and_title(df):
    df, categories = base_lexical_analyzer.get_categories_corpus_and_title(df, WORDS, THEME_CATEGORIES)
    return df, categories