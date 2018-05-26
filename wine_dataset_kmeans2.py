import numpy as np
from sklearn import datasets,cluster
from sklearn.datasets import load_wine
wine=load_wine()
test_index=[10,100,150]
train_target=np.delete(wine.target,test_index)
train_data=np.delete(wine.data,test_index,axis=0)
test_target=wine.target[test_index]
test_data=wine.data[test_index]
k_means=cluster.KMeans(n_clusters=2)
k_means.fit(train_data)
print(k_means.labels_[::10])
print(train_target[::10])