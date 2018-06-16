from sklearn.datasets import load_iris
# from sklearn.datasets import load_wine
# print(load_wine())

import numpy as np
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB

classifier = SVC()
classifier2 = DecisionTreeClassifier()
classifier3 = BernoulliNB()
classifier4 = GaussianNB()

data = load_iris(return_X_y=True)
train_x= data[0]
train_y= data[1]

classifier.fit(train_x, train_y)
classifier2.fit(train_x, train_y)
classifier3.fit(train_x, train_y)
classifier4.fit(train_x, train_y)

s = np.arange(train_x.shape[0])

np.random.shuffle(s)
# print(s)
train_x = train_x[s]
train_y = train_y[s]

print("train_x : ",train_x)
print("train_y : ",train_y)

# test_x = train_x[45:55]
test_y = train_y[45:55]
test_x = np.array([5.8,2.3,3.9,1.5]).reshape(1,-1)
print("test_x : ",test_x)
print("test_y      : ",test_y)
prediction = classifier.predict(test_x)
prediction2 = classifier2.predict(test_x)
prediction3 = classifier3.predict(test_x)
prediction4 = classifier4.predict(test_x)

print("SVC         :",prediction)
print("DecisionTre :",prediction2)
print("BernoulliNB :",prediction3)
print("GaussianNB  :",prediction4)