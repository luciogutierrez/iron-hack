import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# load iris data
iris = load_iris()
print(iris.data.shape)
print(iris.feature_names)

# create X and y matrices with all feature values
X = iris.data
y = iris.target

# plot the first two features as a scatter plot
plt.scatter(X[:,0], X[:,1], c=y)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()

# Genérame un historama con las longitudes de sépalo y de pétalo
plt.hist(X[:,2])
plt.xlabel(iris.feature_names[2])
plt.show()

# creamos un train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# creamos una red neuronal de sklearn con una capa de 4 neuronas
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(4,), activation='relu', max_iter=2000,
                    alpha=1e-4, solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)

print(mlp.score)

# Let's play with TensorFlow
import tensorflow as tf

# load fashion MNIST data
fashion_mnist = tf.keras.datasets.fashion_mnist

# visualize MNIST data first image in train set.
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
plt.imshow(X_train[0])
plt.show()

# visualize the 9 images as a 3x3 grid
plt.figure(figsize=(10,10))
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(X_train[i], cmap='gray', interpolation='none')
    plt.xticks([])
    plt.yticks([])
plt.show()

# Build a convolutional neural network model with Keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, Dropout

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# visualize learned model
from keras.utils import plot_model
plot_model(model, to_file='model.png', show_shapes=True)