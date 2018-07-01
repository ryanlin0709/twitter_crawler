# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Importing the dataset
dataset = pd.read_csv('All5_influencer_information_over_1000.csv')
X = dataset.iloc[:, 1:23].values
y = dataset.iloc[:, 23].values

for i in range(0,len(y)):
    temp = y[i] +1
    y[i] = math.log(temp)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Applying PCA
from sklearn.decomposition import PCA
pca =PCA(n_components = 12)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance =pca.explained_variance_ratio_


from sklearn.model_selection import KFold
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense

def build_classifier():
    classifier = Sequential()
    classifier.add(Dense(units = 11, kernel_initializer = 'normal', activation = 'relu', input_dim = 22))
    classifier.add(Dense(units = 11, kernel_initializer = 'normal', activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'normal'))
    classifier.compile(optimizer = 'rmsprop', loss = 'mean_squared_error', metrics=['mae'])
    return classifier


seed = 7
np.random.seed(seed)
#Regression
estimator = KerasRegressor(build_fn = build_classifier, epochs = 512, batch_size = 32, verbose=0)
estimator.fit(X_train, y_train)
y_pred = estimator.predict(X_test)


kfold = KFold(n_splits=10, random_state = seed)
results = cross_val_score(estimator, X_train, y_train, cv = kfold)
print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm9 = confusion_matrix(test_90, pred_90)

#Applying Gird Search
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
def build_classifier(optimizer):
    classifier = Sequential()
    classifier.add(Dense(units = 11, kernel_initializer = 'normal', activation = 'relu', input_dim = 22))
    classifier.add(Dense(units = 11, kernel_initializer = 'normal', activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'normal'))
    classifier.compile(optimizer = optimizer, loss = 'mean_squared_error', metrics=['mae'])
    return classifier

classifier = KerasClassifier(build_fn = build_classifier)
parameters = {'batch_size': [10, 25, 32, 50, 64], 
              'epochs': [32, 64, 128, 256, 512, 1024],
              'optimizer': ['adam', 'rmsprop']}

grid_search = GridSearchCV(estimator = classifier,
                           param_grid = parameters,
                           scoring = 'mean_squared_error',
                           cv = 10)

grid_search = grid_search.fit(X_train, y_train)
best_parameters = grid_search.best_params_
best_accuracy = grid_search.best_score_
