# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:01:13 2019

@author: Siyuan
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

mpg = pd.read_csv('mpg.csv', index_col = 0)

plt.figure(figsize=(10,8))
plt.subplot(2, 2, 1)
ax1 = plt.gca()
ax1.plot(mpg[mpg['drv']=='f']['displ'],mpg[mpg['drv']=='f']['cty'],'o',c='orange',label='FWD')
ax1.plot(mpg[mpg['drv']=='4']['displ'],mpg[mpg['drv']=='4']['cty'],'o',c='k', label='4WD' )
ax1.plot(mpg[mpg['drv']=='r']['displ'],mpg[mpg['drv']=='r']['cty'],'o',c='deepskyblue',label='RWD')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
plt.legend(title='drive train',frameon=False)
plt.xlabel('displacement (I)')
plt.ylabel('fuel economy (mpg)')

plt.subplot(2, 2, 2)
ax2 = plt.gca()
ax2.plot(mpg[mpg['drv']=='f']['displ'],mpg[mpg['drv']=='f']['cty'],'o',c='orange',label='FWD',alpha=0.3)
ax2.plot(mpg[mpg['drv']=='4']['displ'],mpg[mpg['drv']=='4']['cty'],'o',c='k', label='4WD',alpha=0.3)
ax2.plot(mpg[mpg['drv']=='r']['displ'],mpg[mpg['drv']=='r']['cty'],'o',c='deepskyblue',label='RWD',alpha=0.3)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.legend(title='drive train',frameon=False)
plt.xlabel('displacement (I)')
plt.ylabel('fuel economy (mpg)')

plt.subplot(2, 2, 3)
ax3 = plt.gca()
mu = 1
sigma = 0.02
size = len(mpg)
displ=mpg['displ']*np.random.normal(mu,sigma,size)
cty=mpg['cty']*np.random.normal(mu,sigma,size)
ax3.plot(displ[mpg['drv']=='f'],cty[mpg['drv']=='f'],'o',c='orange',label='FWD',alpha=0.3)
ax3.plot(displ[mpg['drv']=='4'],cty[mpg['drv']=='4'],'o',c='k', label='4WD',alpha=0.3)
ax3.plot(displ[mpg['drv']=='r'],cty[mpg['drv']=='r'],'o',c='deepskyblue',label='RWD',alpha=0.3)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
plt.legend(title='drive train',frameon=False)
plt.xlabel('displacement (I)')
plt.ylabel('fuel economy (mpg)')

plt.subplot(2, 2, 4)
ax4 = plt.gca()
mu = 1
sigma = 0.1
size = len(mpg)
displ=mpg['displ']*np.random.normal(mu,sigma,size)
cty=mpg['cty']*np.random.normal(mu,sigma,size)
ax4.plot(displ[mpg['drv']=='f'],cty[mpg['drv']=='f'],'o',c='orange',label='FWD',alpha=0.3)
ax4.plot(displ[mpg['drv']=='4'],cty[mpg['drv']=='4'],'o',c='k', label='4WD',alpha=0.3)
ax4.plot(displ[mpg['drv']=='r'],cty[mpg['drv']=='r'],'o',c='deepskyblue',label='RWD',alpha=0.3)
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)
plt.legend(title='drive train',frameon=False)
plt.xlabel('displacement (I)')
plt.ylabel('fuel economy (mpg)')

plt.suptitle('Fuel economy vs displacement', fontsize = 15, y = 0.93)




