# JUST the code for randomForestClassifier using sci-kit learn. same code as in 
# Pandas&Scikit.ipynb, but without the markdowns

import sklearn
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as met
import matplotlib.pyplot as plt

# -------- READING --------
fdata = pd.read_csv("03PyDataScience/flower_dataset.csv")

# -------- PREPROCESSING: ENCODING ---------
# converting nonnumeric to numeric for random forest classification: using labelEncoder
# species column is not ordinal, but i don't feel like messing with onehot encoding rn
lblEncoder = LabelEncoder()

# remember: use iloc for accessing columns by numerical index. .iloc[rows, columns]
encData = pd.DataFrame()
encData["species_enc"] = fdata["species"].map({'rose':4, 'shoeblack plant':14, 'hibiscus':8})
encData[["size_enc", "frag_enc"]] = fdata.iloc[:, 1:-1].apply(lblEncoder.fit_transform)

# use concat to insert encoded columns after original ones and before height column
# considering fdata to be 2 frames (up to index 2 and index 3) and encData
insertAt = fdata.columns.get_loc("height_cm")
fdata = pd.concat([fdata.iloc[:, :insertAt], encData, fdata.iloc[:, insertAt:]], axis=1)

# assuming target label is species (rose, shoeblack plant, or hibiscus)
# dataframe drop method drops the specified row/column and keeps the rest of
# the dataframe (axis=0 for index, axis=1 for columns). here drop up to encoded size column
y = fdata["species_enc"]
X = fdata.drop(fdata.iloc[:, :fdata.columns.get_loc("size_enc")], axis=1)

# pandas value_counts shows counts of unique values, ex. how many of each
# species is in the dataset
print(y.value_counts())

# -------- PREPROCESSING: DIVIDING INTO TEST AND TRAIN --------
# input X and Y and unpack into 4 lists. show shapes of these lists 
# at this point, data is ready to apply a model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(X_train)

# --------- SETTING UP CLASSIFIER --------
clf = RandomForestClassifier()
# use get_params() to see the current parameters for the classifier. leave 
# as default for now
clf.get_params()

# in order to use the fit() method, nonnumeric data has to be converted to numeric
# fitting data to model
clf.fit(X=X_train, y=y_train)

# --------- PREDICTING AND CHECKING ACCURACY --------
y_predict = clf.predict(X=X_test)

# checking accuracy:
train_acc = met.accuracy_score(y_test, y_predict)
print(f"accuracy is: {train_acc*100:.2f}%")

#from sklearn.metrics import confusion_matrix
cm = met.confusion_matrix(y_test, y_predict)
cmPlot = met.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["rose","shoeblack","hibiscus"]).plot()
plt.show()