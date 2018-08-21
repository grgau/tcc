#!/usr/bin/python3

import pandas as pd

input_file="/home/pedroh/dataset_2018.csv"
df = pd.read_csv(input_file, low_memory=False)

print(df.groupby('Label').count())
