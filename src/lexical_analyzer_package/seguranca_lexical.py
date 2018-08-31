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
STEMMED_WORDS = ['violência', 
                 'assalto', 'assaltad', 
                 'sequestro', 'sequestrad', 
                 'presídio', 'presidiári', 'penitenciári',
                 'preso', 'presa'
                 'assassinato', 
                 'crime', 'criminos',
                 'julgamento', 
                 'condenaç', 'condenad',
                 'fuga',
                 'ladr', 
                 'segurança',
                 'polícia']

THEME_CATEGORIES = ['violência', 
                    'assalto', 'assalto', 
                    'sequestro', 'sequestro', 
                    'presídio', 'presídio', 'presídio', 
                    'preso', 'preso'
                    'assassinato', 
                    'crime', 'crime', 
                    'julgamento', 
                    'condenação', 'condenação', 
                    'fuga',
                    'ladrão',
                    'segurança']

def lexical(df):
    df, categories = base_lexical_analyzer.get_categories_corpus(df, STEMMED_WORDS, THEME_CATEGORIES)
    return df, categories
 
def lexical_corpus_and_title(df):
    df, categories = base_lexical_analyzer.get_categories_corpus_and_title(df, STEMMED_WORDS, THEME_CATEGORIES)
    return df, categories