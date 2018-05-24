import random
from scipy.spatial import distance
def euc(a, b):
	return distance.euclidean(a,b)
class MyKNN():
	def fit(self, x_train, y_train):
		self.x_train= x_train
		self.y_train= y_train
	def predict(self, x_test):
		predictions = []
		for row in x_test:
			label = self.closest(row)
			predictions.append(label)
		return predictions
	def closest(self, row):
		best_dist = euc(row, self.x_train[0])
		best_index=0
		for i in range(1, len(self.x_train)):
			dist = euc(row, self.x_train[i])
			if dist < best_dist:
				best_dist= dist
				best_index= i
		return  self.y_train[best_index]
from sklearn import datasets
breast_cancer = datasets.load_breast_cancer()
x=breast_cancer.data
y=breast_cancer.target
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)
my_clf=MyKNN()
my_clf.fit(x_train,y_train)
predictions=my_clf.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))
