from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
# from sklearn.datasets import load_iris
# print(load_iris())

classifier = SVC()
classifier2 = DecisionTreeClassifier()
classifier3 = BernoulliNB()
classifier4 = GaussianNB()

# shape,size,color
# spherical,oval,long
# small,medium,large

train_x = [[0,1,0],[0,2,1],[1,2,2],
           [0,1,2],[2,1,2],[0,0,1],
           [0,0,1],[0,0,1],[0,0,1],
           [0,1,0],[0,1,0],[0,2,1]]

train_y = [0,1,2,
           3,4,5,
           5,5,5,
           0,0,1]

test_x = [[1,2,2],[0,1,0]]
# test_y = [2,5]
classifier.fit(train_x,train_y)
classifier2.fit(train_x,train_y)
classifier3.fit(train_x,train_y)
classifier4.fit(train_x,train_y)
prediction = classifier.predict(test_x)
prediction2 = classifier2.predict(test_x)
prediction3 = classifier3.predict(test_x)
prediction4 = classifier4.predict(test_x)

print("prediction  :",prediction)
print("prediction2 :",prediction2)
print("prediction3 :",prediction3)
print("prediction4 :",prediction4)
