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
WORDS_CASE_SENSITIVE = ['Susp', 'SUSP', 'DEPEN', 'SENASP', 'PRF', 'PF']

THEME_CATEGORIES_CASE_SENSITIVE = ['susp', 'susp', 'depen', 'senasp', 'prf', 'pf']

WORDS = ['jungmann', 'segurança pública', 'penitenciária', 'intervenção', 'defesa', 'tráfico', 'fronteira', 'drogas',
         'violência', 
         'assalto', 'assaltad', 
         'sequestro', 'sequestrad', 
         'presídio', 'presidiári',
         'preso',
         'assassinato', 
         'crime', 'criminos',
         'julgamento', 
         'condenaç', 'condenad',
         'fuga',
         'ladr', 
         'polícia'
         ]

THEME_CATEGORIES = ['jungmann', 'segurança pública', 'penitenciária', 'intervenção', 'defesa', 'tráfico', 'fronteira', 'drogas',
                    'violência', 
                    'assalto', 'assalto', 
                    'sequestro', 'sequestro', 
                    'presídio', 'presídio', 
                    'preso',
                    'assassinato', 
                    'crime', 'crime', 
                    'julgamento', 
                    'condenação', 'condenação', 
                    'fuga',
                    'ladrão',
                    'polícia'
                    ]


def lexical(df):
    df, categories = base_lexical_analyzer.get_categories_corpus(df, WORDS, THEME_CATEGORIES, WORDS_CASE_SENSITIVE, THEME_CATEGORIES_CASE_SENSITIVE)
    return df, categories
 
def lexical_corpus_and_title(df):
    df, categories = base_lexical_analyzer.get_categories_corpus_and_title(df, WORDS, THEME_CATEGORIES, WORDS_CASE_SENSITIVE, THEME_CATEGORIES_CASE_SENSITIVE)
    return df, categories
