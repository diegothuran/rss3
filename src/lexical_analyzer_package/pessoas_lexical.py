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
WORDS = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'sergio moro', 'hamilton mourão',
         'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto']

THEME_CATEGORIES = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'sérgio moro', 'hamilton mourão',
                    'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto']

def lexical(df):
    df, categories = base_lexical_analyzer.get_categories_corpus(df, WORDS, THEME_CATEGORIES)
    return df, categories
 
def lexical_corpus_and_title(df):
    df, categories = base_lexical_analyzer.get_categories_corpus_and_title(df, WORDS, THEME_CATEGORIES)
    return df, categories

