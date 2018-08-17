#!/usr/bin/python3

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, cross_val_predict

def naiveBayesGaussianCL(df, testSize, features):
    # Naive Bayes Gaussian

    clf = GaussianNB().fit(X_train, y_train)
    scores = cross_val_score(clf, df[features], df["Label"], cv=5)
    pred = cross_val_predict(clf, df[features], df["Label"], cv=5)

    p_gnb = clf.predict(X_test)

    #print(clf.score(X_test, y_test))
	print("" + scores.mean() + "," + scores.std() * 2 + " // " + "testSize: " + testSize)
    #print(classification_report(y_test, p_gnb))
    #print(pred)
    #print(confusion_matrix(y_test, p_gnb))


def naiveBayesMultinomialCL(df, testSize, features):
    # Naive Bayes Multinomial

    clf = MultinomialNB().fit(X_train, y_train)
    scores = cross_val_score(clf, df[features], df["Label"], cv=5)
    pred = cross_val_predict(clf, df[features], df["Label"], cv=5)

    p_gnb = clf.predict(X_test)

    #print(clf.score(X_test, y_test))
	print("" + scores.mean() + "," + scores.std() * 2 + " // " + "testSize: " + testSize)
    #print(classification_report(y_test, p_gnb))
    #print(pred)
    #print(confusion_matrix(y_test, p_gnb))
