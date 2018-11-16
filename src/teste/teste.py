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

site = 'bbc'
# estrutura tupla = (id, site, relevancia)
# tupla = relevancia_site_table.select(site)


dates = [datetime.date(2018, 11, 1), datetime.date(2018, 11, 2), datetime.date(2018, 11, 3), datetime.date(2018, 11, 4), 
         datetime.date(2018, 11, 5), datetime.date(2018, 11, 6), datetime.date(2018, 11, 7), datetime.date(2018, 11, 8),
         datetime.date(2018, 11, 9), datetime.date(2018, 11, 10), datetime.date(2018, 11, 11), datetime.date(2018, 11, 12), datetime.date(2018, 11, 13)]
for date in dates:
    relevancia_site_table.select_form_date(date)
