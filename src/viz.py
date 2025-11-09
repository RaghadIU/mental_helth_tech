import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_scatter(df, x_col, y_col, hue=None, title=None, save_path=None):
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, palette='tab10')
    if title:
        plt.title(title)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def plot_heatmap(df, title=None, save_path=None):
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    if title:
        plt.title(title)
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def plot_radar(df, features, group_col, save_path=None):
    import matplotlib.pyplot as plt
    import numpy as np

    labels=np.array(features)
    n_labels = len(labels)

    groups = df[group_col].unique()
    angles = np.linspace(0, 2 * np.pi, n_labels, endpoint=False).tolist()
    angles += angles[:1]  # close the loop

    plt.figure(figsize=(6,6))

    for g in groups:
        values = df[df[group_col]==g][features].mean().tolist()
        values += values[:1]  # close the loop
        plt.polar(angles, values, label=f'Cluster {g}')
    
    plt.xticks(angles[:-1], labels)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3,1.1))
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()
