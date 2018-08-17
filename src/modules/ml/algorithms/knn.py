#!/usr/bin/python3

def knnCL (df, testSize, features):
    # KNN (5 Neighbors)

    knn = KNeighborsClassifier().fit(X_train, y_train)
    scores = cross_val_score(knn, df[features], df["Label"], cv=5)
    pred = cross_val_predict(knn, df[features], df["Label"], cv=5)

    p_knn = knn.predict(X_test)

    #print(knn.score(X_test, y_test))
	print("" + scores.mean() + "," + scores.std() * 2 + " // " + "testSize: " + testSize)
    #print(classification_report(y_test, p_knn))
    #print(pred)
    #print(confusion_matrix(y_test, p_knn))
