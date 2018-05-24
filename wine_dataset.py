import numpy as np
from sklearn.datasets import load_wine
from sklearn import tree
wine=load_wine()
test_index=[10,100,150]
train_target=np.delete(wine.target,test_index)
train_data=np.delete(wine.data,test_index,axis=0)
test_target=wine.target[test_index]
test_data=wine.data[test_index]
clf=tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)
print(test_target)
print(clf.predict(test_data))

print(wine.target)