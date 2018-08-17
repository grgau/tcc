#!/usr/bin/python3

from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, cross_val_predict

def decisionTreeCL(df, testSize, features):
    # Decision tree

	X_train, X_test, y_train, y_test = train_test_split(df[features], df["Label"], test_size=testSize)      # Define conjuntos de treino e de teste

	clf = tree.DecisionTreeClassifier().fit(X_train,y_train)
	scores = cross_val_score(clf, df[features], df["Label"], cv=5)
	pred = cross_val_predict(clf, df[features], df["Label"], cv=5)

	p_tree = clf.predict(X_test)

	#print(clf.score(X_test, y_test))
	print("Decision Tree: " + scores.mean() + "," + scores.std() * 2 + " // " + "testSize: " + testSize)
	#print(classification_report(y_test, p_tree))
	#print(pred)
	#print(confusion_matrix(y_test, p_tree))

def randomForestCL(df, testSize, features):
	# Random forest

	clf = RandomForestClassifier(n_estimators=10).fit(X_train, y_train)
	scores = cross_val_score(clf, df[features], df["Label"], cv=5)
	pred = cross_val_predict(clf, df[features], df["Label"], cv=5)

	p_tree = clf.predict(X_test)

	"""
	importances = clf.feature_importances_
	indices = np.argsort(importances)[::-1]
	for f in range(X_train.shape[1]):
    	print("%2d) %-*s %f" % (f + 1, 30, features[indices[f]],importances[indices[f]]))
	"""

	#print(clf.score(X_test, y_test))
	print("" + scores.mean() + "," + scores.std() * 2 + " // " + "testSize: " + testSize)
	#print(classification_report(y_test, p_tree))
	#print(pred)
	#print(confusion_matrix(y_test, p_tree))
