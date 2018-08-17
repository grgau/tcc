#!/usr/bin/python3

from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, cross_val_predict

def knnCL (df, testSize, features):
	# KNN (5 Neighbors)

	X_train, X_test, y_train, y_test = train_test_split(df[features], df["Label"], test_size=testSize)      # Define conjuntos de treino e de teste
	
	knn = KNeighborsClassifier().fit(X_train, y_train)
	scores = cross_val_score(knn, df[features], df["Label"], cv=5)
	pred = cross_val_predict(knn, df[features], df["Label"], cv=5)

	p_knn = knn.predict(X_test)

	#print(knn.score(X_test, y_test))
	print("KNN:\t\t" + str(scores.mean()) + "\t" + str(scores.std() * 2) + "\t" + "testSize: " + str(testSize))
	#print(classification_report(y_test, p_knn))
	#print(pred)
	#print(confusion_matrix(y_test, p_knn))
