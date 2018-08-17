#!/usr/bin/python3
import pandas as pd
from sklearn.cross_validation import train_test_split
import gc

from .algorithms.decisionTree import decisionTreeCL
"""from .algorithms.naiveBayesGaussian import naiveBayesGaussianCL
from .algorithms.naiveBayesMultinomial import naiveBayesMultinomialCL
from .algorithms.randomForest import randomForestCL
from .algorithms.svm import svmLinearCL
from .algorithms.svm import svmPolyCL
from .algorithms.svm import svmRBFCL
"""

def readCSV (dataset):
    df = pd.read_csv(dataset)
    return df

def limitDataset (df):
    # Sorteia quantidade de atividades a partir de seu label, sorteando n atividades onde n é o label menos frequente
    n = min(df.groupby(['Label']).size())
    df_list = []
    for i in range (1,11):
        if not df[df['Label'] == i].empty:
            df_list.append(df[df['Label'] == i].sample(n))

    df = pd.concat(df_list)
    return df

def proProcessing(dataset, duplicate):
    df = readCSV(dataset)   # Ler dataset
    df = limitDataset(df)   # Limitar quantidade de dados pelo label de menor quantidade

    # Se receber parametro de dropar duplicados
    if duplicate:
        None
    else:
        df = df.drop_duplicates()

    # One-hot Encoding da coluna 'Protocolo' e reordenacao de colunas
    df = pd.get_dummies(df, columns = ['Protocolo'])
    df = df[['Duracao', 'Qtd_fluxos', 'Unique_dst_ports', 'Protocolo_1', 'Protocolo_6', 'Protocolo_17', 'Pcts_min', 'Pcts_max', 'Pcts_mean', 'Pcts_std', 'Pcts_total', 'Bytes_min', 'Bytes_max', 'Bytes_mean', 'Bytes_std', 'Bytes_total', 'Qtd_urg', 'Qtd_ack', 'Qtd_psh', 'Qtd_rst', 'Qtd_syn', 'Qtd_fin', 'Label']]

    return df

def defineTestSize(df, testSize):
    features = list(df.columns[:20])    # Define as colunas de features
    X_train, X_test, y_train, y_test = train_test_split(df[features], df["Label"], test_size=testSize)      # Define conjuntos de treino e de teste
    return X_train, X_test, y_train, y_test, features

def classify (dataset):
    df = proProcessing(dataset, 1)      # Com duplicatas
    X_train, X_test, y_train, y_test, features = defineTestSize(df, 0.5)    # testSize = 0.5

    # Aplica algoritmos de classificacao
    decisionTreeCL(df, X_train, X_test, y_train, features)


    X_train, X_test, y_train, y_test, features = defineTestSize(df, 0.3)    # testSize = 0.3

    # Aplica algoritmos de classificacao
    decisionTreeCL(df, X_train, y_train, X_test, features)

    # Limpa df da memória
    del df
    gc.collect()
    ##############################################################

    df = proProcessing(dataset, 0)      # Com duplicatas
    X_train, X_test, y_train, y_test, features = defineTestSize(df, 0.5)    # testSize = 0.5

    # Aplica algoritmos de classificacao
    decisionTreeCL(df, X_train, y_train, X_test, features)


    X_train, X_test, y_train, y_test, features = defineTestSize(df, 0.3)    # testSize = 0.3

    # Aplica algoritmos de classificacao
    decisionTreeCL(df, X_train, y_train, X_test, features)
