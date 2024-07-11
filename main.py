import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pickle
from sklearn.model_selection import  train_test_split

#importing the dataset
dataset = pd.read_csv("data.csv")

#dataset analysis
print(dataset.info())
print(dataset.describe())
print(dataset.head())

# correlations
attributes = ['age','gender', 'fbs','thalach']
scatter_matrix(dataset[attributes], figsize=(12,8))
dataset.plot(kind="scatter", x ='age', y='thalach', alpha=0.8)

# Data preprocessing
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
dataset[columns] = sc.fit_transform(dataset[columns])
print(dataset.head())

# split the dataset
X = dataset.iloc[:,: -1].values
y = dataset.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,random_state=42 )

# Training the model

# classifier = LogisticRegression(random_state=0)
classifier = KNeighborsClassifier(n_neighbors = 5)
# classifier  = SVC(kernel="poly")
# classifier = DecisionTreeClassifier( random_state=0)
# classifier = RandomForestClassifier(n_estimators=10, criterion="entropy", random_state=0)
classifier.fit(X_train, y_train)

score = classifier.score(X_train, y_train)
print(score)

# Predciting the test set results

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Making the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("the confusion matrix is \n ",cm)
a_score = accuracy_score(y_test, y_pred)
print(a_score)

# 24 persons correctly predicted by the model to have the heart disease
# 5 person incorrectly predicted by the model to have the heart disease
# 3 people incorrectly predicted by the model to not have the heart disease
# 29 people correctly predicted by the modal to have the heart disease

# Saving the model 


with open("model", "wb") as f :
    pickle.dump(classifier, f)


