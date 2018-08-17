#!/usr/bin/python3

from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, cross_val_predict

def svmLinearCL(df, testSize, features):
    # Svm linear

    C = 1.0
    svc = svm.SVC(kernel='linear', C=C).fit(X_train, y_train)
    scores = cross_val_score(svc, df[features], df["Label"], cv=5)
    pred = cross_val_predict(svc, df[features], df["Label"], cv=5)

    p_svm = svc.predict(X_test)

    #print(svc.score(X_test, y_test))
	print("" + scores.mean() + "," + scores.std() * 2 + " // " + "testSize: " + testSize)
    #print(classification_report(y_test, p_svm))
    #print(pred)
    #print(confusion_matrix(y_test, p_svm))

def svmPolyCL(df, testSize, features):
    # Svm Poly=2

    C = 1.0
    svc = svm.SVC(kernel="poly", degree=2, C=C).fit(X_train, y_train)
    scores = cross_val_score(svc, df[features], df["Label"], cv=5)
    pred = cross_val_predict(svc, df[features], df["Label"], cv=5)

    p_svm = svc.predict(X_test)

    #print(svc.score(X_test, y_test))
    print(scores.mean(), scores.std() * 2 + " // " + "testSize: " + testSize)
    #print(classification_report(y_test, p_svm))
    #print(pred)
    #print(confusion_matrix(y_test, p_svm))

def svmRBFCL(df, testSize, features):
    # Svm RBF

    C = 1.0
    svc = svm.SVC(kernel='rbf', C=C).fit(X_train, y_train)
    scores = cross_val_score(svc, df[features], df["Label"], cv=5)
    pred = cross_val_predict(svc, df[features], df["Label"], cv=5)

    p_svm = svc.predict(X_test)

    #print(svc.score(X_test, y_test))
	print("" + scores.mean() + "," + scores.std() * 2 + " // " + "testSize: " + testSize)
    #print(classification_report(y_test, p_svm))
    #print(pred)
    #print(confusion_matrix(y_test, p_svm))
