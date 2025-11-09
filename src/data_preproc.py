# src/data_preproc.py
import pandas as pd
import numpy as np

def load_csv(file_path):
    return pd.read_csv(file_path)

def load_excel(file_path):
    return pd.read_excel(file_path)

def handle_missing_values(df, strategy='median'):
    df_copy = df.copy()
    for col in df_copy.columns:
        if df_copy[col].dtype in ['float64','int64']:
            if strategy == 'median':
                df_copy[col] = df_copy[col].fillna(df_copy[col].median())
            elif strategy == 'mean':
                df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
        elif df_copy[col].dtype in ['bool', 'object']:
            df_copy[col] = df_copy[col].fillna(df_copy[col].mode()[0])
    return df_copy


def encode_categorical(df, columns=None):
    if columns is None:
        columns = df.select_dtypes(include=['object']).columns.tolist()
    df_encoded = pd.get_dummies(df, columns=columns, drop_first=True)
    return df_encoded
