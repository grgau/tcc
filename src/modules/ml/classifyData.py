#!/usr/bin/python3
import pandas as pd
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
    df = pd.read_csv(dataset, low_memory=False)
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

def preProcessing(dataset, duplicate):
    df = readCSV(dataset)   # Ler dataset

    # Se receber parametro de dropar duplicados
    if duplicate:
        None
    else:
        df = df.drop_duplicates()

    df = limitDataset(df)   # Limitar quantidade de dados pelo label de menor quantidade

    # One-hot Encoding da coluna 'Protocolo' e reordenacao de colunas
    df = pd.get_dummies(df, columns = ['Protocolo'])
    df = df[['Duracao', 'Qtd_fluxos', 'Unique_dst_ports', 'Protocolo_1', 'Protocolo_6', 'Protocolo_17', 'Pcts_min', 'Pcts_max', 'Pcts_mean', 'Pcts_std', 'Pcts_total', 'Bytes_min', 'Bytes_max', 'Bytes_mean', 'Bytes_std', 'Bytes_total', 'Qtd_urg', 'Qtd_ack', 'Qtd_psh', 'Qtd_rst', 'Qtd_syn', 'Qtd_fin', 'Label']]

    return df

#def defineTestSize(df, testSize):
#    features = list(df.columns[:20])    # Define as colunas de features
#    X_train, X_test, y_train, y_test = train_test_split(df[features], df["Label"], test_size=testSize)      # Define conjuntos de treino e de teste
#    return X_train, X_test, y_train, y_test, features

def classify (dataset):
	df = preProcessing(dataset, 1)      # Com duplicatas
	features = list(df.columns[:20])    # Define as colunas de features
    
	# Aplica algoritmos de classificacao
	decisionTreeCL(df, 0.5, features)
	decisionTreeCL(df, 0.3, features)

	# Limpa df da memória
	#del df
	#gc.collect()

	##############################################################

	df = preProcessing(dataset, 0)      # Sem duplicatas
	features = list(df.columns[:20])	# Define as colunas de features

    # Aplica algoritmos de classificacao
	decisionTreeCL(df, 0.5, features)
	decisionTreeCL(df, 0.3, features)

