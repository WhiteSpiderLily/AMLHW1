# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 23:16:33 2019

@author: Siyuan
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import matplotlib.patches as mpatches

iris = datasets.load_iris()
iris_data = iris.data
iris_ind = iris.target
SL = iris_data[:,0]
SW = iris_data[:,1]
PL = iris_data[:,2]
PW = iris_data[:,3]
Array = {}

Array[1] = SL[iris_ind == 0]
Array[2] = SL[iris_ind == 1]
Array[3] = SL[iris_ind == 2]
Array[4] = SW[iris_ind == 0]
Array[5] = SW[iris_ind == 1]
Array[6] = SW[iris_ind == 2]
Array[7] = PL[iris_ind == 0]
Array[8] = PL[iris_ind == 1]
Array[9] = PL[iris_ind == 2]
Array[10] = PW[iris_ind == 0]
Array[11] = PW[iris_ind == 1]
Array[12] = PW[iris_ind == 2]


plt.figure(figsize=(10,10))
for i in range(1,5):
    for j in range(1,5):
        ax = plt.subplot(4,4,(i-1)*4+j)
        if i == j:
            array = np.concatenate((Array[(i-1)*3+1],Array[(i-1)*3+2],Array[(i-1)*3+3]))
            plt.hist(array, bins = 20, edgecolor = 'black')
        else:
            ax.plot(Array[(j-1)*3+1],Array[(i-1)*3+1], 'o' , c = 'b', markersize = 3, label = 'setosa')
            ax.plot(Array[(j-1)*3+2],Array[(i-1)*3+2], 'o' , c = 'r', markersize = 3, label = 'versicolor')
            ax.plot(Array[(j-1)*3+3],Array[(i-1)*3+3], 'o' , c = 'g', markersize = 3, label = 'virginica')
        if j == 1:
            if i == 1:
                plt.ylabel('Sepal Length (cm)')
            elif i == 2:
                plt.ylabel('Sepal Width (cm)')
            elif i == 3:
                plt.ylabel('Petal Length (cm)')
            else:
                plt.ylabel('Petal Width (cm)')
        if i == 4:
            if j == 1:
                plt.xlabel('Sepal Length (cm)')
            elif j ==2:
                plt.xlabel('Sepal Width (cm)')
                plt.legend(bbox_to_anchor=(2.2, -0.3), ncol=3)
            elif j ==3:
                plt.xlabel('Petal Length (cm)')
            else:
                plt.xlabel('Petal Width (cm)')

fig = plt.gcf()
fig.suptitle('Pair plot of the Iris dataset, colored by class label', y = 0.93, fontsize = 15)



