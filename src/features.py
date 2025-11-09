# src/features.py
import pandas as pd

def create_work_life_balance_score(df, hours_col='hours_worked', stress_col='stress_level'):

    df_copy = df.copy()
    # Normalize columns
    df_copy[hours_col] = (df_copy[hours_col] - df_copy[hours_col].min()) / (df_copy[hours_col].max() - df_copy[hours_col].min())
    df_copy[stress_col] = (df_copy[stress_col] - df_copy[stress_col].min()) / (df_copy[stress_col].max() - df_copy[stress_col].min())
    # Inverse relation: less hours & stress => higher balance
    df_copy['work_life_balance'] = 1 - 0.5*(df_copy[hours_col] + df_copy[stress_col])
    return df_copy

def create_stress_index(df, columns):
    df_copy = df.copy()
    df_copy['stress_index'] = df_copy[columns].mean(axis=1)
    return df_copy
