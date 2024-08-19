# KNN is like a voting system, where majority class label among the 
# k closest neighbors determines the class label of the current point. 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn 
import sklearn.metrics as met
import math

fdata = pd.read_csv("03PyDataScience/flower_dataset.csv")

# converting to numeric data
from sklearn.preprocessing import LabelEncoder
lblEncoder = LabelEncoder()
encData = pd.DataFrame()
encData["species_enc"] = fdata["species"].map({'rose':4, 'shoeblack plant':14, 'hibiscus':8})
encData[["size_enc", "frag_enc"]] = fdata.iloc[:, 1:-1].apply(lblEncoder.fit_transform)
insertAt = fdata.columns.get_loc("height_cm")
fdata = pd.concat([fdata.iloc[:, :insertAt], encData, fdata.iloc[:, insertAt:]], axis=1)
print(fdata.head())

# check types
print(fdata.info())
# check for missing values
print(fdata.isnull().sum())

# split dataset 
from sklearn.model_selection import train_test_split
y = fdata["species_enc"]
X = fdata.drop(fdata.iloc[:, :fdata.columns.get_loc("size_enc")], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
print(X_train)

# train model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 10)
knn.fit(X_train, y_train)

# make prediction 
y_predict = knn.predict(X_test)

# find accuracy
knn_acc = round(met.accuracy_score(y_test, y_predict))
print("accuracy: ", knn_acc*100)

# confusion matrix
cm = met.confusion_matrix(y_test, y_predict)
cmPlot = met.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["rose","shoeblack","hibiscus"]).plot()
plt.show()