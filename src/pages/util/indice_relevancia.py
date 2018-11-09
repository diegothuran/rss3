# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from pages.util import load_pages

from sklearn.preprocessing import MinMaxScaler
import numpy as np
import math

def get_indice_relevancia():
    """
    indice_relevancia = (1 - MinMax(log(X)))
    """
    log_base = []
    for page in load_pages.PAGES:
        if(page.GLOBAL_RANK is not None):
            log_base.append(math.log(page.GLOBAL_RANK))
        else:
            log_base.append(None)
    
    scaled_indices = MinMaxScaler().fit_transform(np.array(log_base).reshape(-1, 1))
    indice_relevancia = 1 - scaled_indices
#     for i in range(len(indice_relevancia)):
#         print(load_pages.PAGES[i])
#         print(indice_relevancia[i])
    return indice_relevancia
