# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:23:25 2018

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import discriminant_analysis, decomposition, tree
from matplotlib.mlab import PCA
from mpl_toolkits.mplot3d import Axes3D
import graphviz

PlotSize = 10

# Data points:
# N = # samples per class
# C = # of classes
# D = # of variables
N = 100
C = 3
D = 250


# N samples per class of D independent gaussian variables each
data = np.random.randn(N*C,D)
classes = np.repeat(np.arange(C),N)

alldata = np.append(data, classes.reshape(N*C,1), 1)
np.savetxt('randdata.csv',alldata,delimiter=',')

# Principal Components
pca = sklearn.decomposition.PCA(n_components=2)
transformed = pca.fit_transform(data)
plt.figure(figsize = (PlotSize, PlotSize))
plt.scatter(transformed[:,0], transformed[:,1], c=classes)
plt.title(str(C) + ' classes, ' + str(D) + ' IID Gaussian dimensions: PCA')
plt.show()

# LDA
lda = sklearn.discriminant_analysis.LinearDiscriminantAnalysis(n_components=2)
transformed = lda.fit_transform(data, classes)
plt.figure(figsize = (PlotSize, PlotSize))
plt.scatter(transformed[:,0], transformed[:,1], c=classes)
plt.title(str(C) + ' classes, ' + str(D) + ' IID Gaussian dimensions: LDA')
plt.show()

# Decision tree
dtree = sklearn.tree.DecisionTreeClassifier()
dtree = dtree.fit(data,classes)
dot_data = tree.export_graphviz(dtree, out_file=None, 
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 
