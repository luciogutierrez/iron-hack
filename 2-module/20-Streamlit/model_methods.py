import numpy as np
import pandas as pd
import random
import pickle

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = load_iris()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=10)
clf = LogisticRegression(C=0.01)
clf.fit(X_train, y_train)
pickle.dump(clf, open('final_model.sav', 'wb'))


