# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:18:47 2019

@author: Siyuan
"""

import pandas as pd
import numpy as np

data = pd.read_csv('input.txt', encoding = 'utf-16', escapechar = '\\', index_col = 0, header = None)

def nrows(data):
    return len(data) - 1

def ncols(data):
    return len(data.iloc[1,:])

def pop(data):
    total = 0
    nrows = len(data)
    for i in range(1,nrows):
        try:
            datum = float(data.iloc[i,-1])
            if not np.isnan(datum):
                total += datum
        except ValueError:
            continue
    return int(total)

def test_rows_cols():
    assert nrows(data) == 225
    assert ncols(data) == 31
    
def test_pop():
    assert pop(data) == 7065