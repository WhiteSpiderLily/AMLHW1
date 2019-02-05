# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 18:32:54 2019

@author: Siyuan
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.lines as mlines

data = pd.read_excel('task2data.xlsx')
x = data.iloc[:,0]
y1 = data.iloc[:,1]
y2 = data.iloc[:,2]
xnew = np.linspace(1999, 2009, num=100, endpoint=True)

f1 = interp1d(x, y1, kind = 'cubic')
f2 = interp1d(x, y2, kind = 'cubic')

plt.figure(figsize=(10,3))
plt.title('US spending on science, space, and technology \n correlates with \n Suicides by hanging, strangulation, and suffocation\n Correlation: 99.79% (r=0.99789126)')
ax1 = plt.gca()
line11 = ax1.plot(x, y1, 'o', c = 'r')
line12 = ax1.plot(xnew, f1(xnew), '-', c = 'r')
plt.yticks([15, 20, 25, 30], ['$15 billion', '$20 billion', '$25 billion', '$30 billion'])
plt.ylabel('US spending on science')
ax2 = ax1.twinx()
line21 = ax2.plot(x, y2, 'o', c = 'black')
line22 = ax2.plot(xnew, f2(xnew), '-', c = 'black')
plt.xticks(x)
plt.yticks([4000, 6000, 8000, 10000], ['4000 suicides', '6000 suicides', '8000 suicides', '10000 suicides'])
plt.ylabel('Hanging suicides')

red_line = mlines.Line2D([], [], color='red', marker='o',
                          markersize=5, label='US spending on science')
black_line = mlines.Line2D([], [], color='k', marker='o',
                          markersize=5, label='Hanging suicides')
plt.legend(handles=[red_line,black_line])