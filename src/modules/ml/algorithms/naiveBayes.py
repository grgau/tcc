#!/usr/bin/python3

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, cross_val_predict

def naiveBayesGaussianCL(df, testSize, features):
    # Naive Bayes Gaussian

	X_train, X_test, y_train, y_test = train_test_split(df[features], df["Label"], test_size=testSize)      # Define conjuntos de treino e de teste
	
	clf = GaussianNB().fit(X_train, y_train)
	scores = cross_val_score(clf, df[features], df["Label"], cv=5)
	pred = cross_val_predict(clf, df[features], df["Label"], cv=5)

	p_gnb = clf.predict(X_test)

    #print(clf.score(X_test, y_test))
	print("NB Gaussian:\t" + str(scores.mean()) + "\t" + str(scores.std() * 2) + "\t" + "testSize: " + str(testSize))
    #print(classification_report(y_test, p_gnb))
    #print(pred)
    #print(confusion_matrix(y_test, p_gnb))


def naiveBayesMultinomialCL(df, testSize, features):
    # Naive Bayes Multinomial

	X_train, X_test, y_train, y_test = train_test_split(df[features], df["Label"], test_size=testSize)      # Define conjuntos de treino e de teste
	
	clf = MultinomialNB().fit(X_train, y_train)
	scores = cross_val_score(clf, df[features], df["Label"], cv=5)
	pred = cross_val_predict(clf, df[features], df["Label"], cv=5)

	p_gnb = clf.predict(X_test)

    #print(clf.score(X_test, y_test))
	print("NB Multi:\t" + str(scores.mean()) + "\t" + str(scores.std() * 2) + "\t" + "testSize: " + str(testSize))
    #print(classification_report(y_test, p_gnb))
    #print(pred)
    #print(confusion_matrix(y_test, p_gnb))
