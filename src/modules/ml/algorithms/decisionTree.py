#!/usr/bin/python3

from sklearn import tree
from sklearn.cross_validation import cross_val_score, cross_val_predict

def decisionTreeCL(df, X_train, X_test, y_train, features):
    # Decision tree

    clf = tree.DecisionTreeClassifier().fit(X_train,y_train)
    scores = cross_val_score(clf, df[features], df["Label"], cv=5)
    pred = cross_val_predict(clf, df[features], df["Label"], cv=5)

    p_tree = clf.predict(X_test)

    #print(clf.score(X_test, y_test))
    print(scores.mean(), scores.std() * 2)
    #print(classification_report(y_test, p_tree))
    #print(pred)
    #print(confusion_matrix(y_test, p_tree))
