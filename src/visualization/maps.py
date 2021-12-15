import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def nan_map(data): #Patrick
    """
    return a figure to detect the Nan values
    """
    plt.figure(figsize=(10,5))
    sns.heatmap(data.isna(),cbar=False)
    plt.show()


def heatmap(data,target) : #Clément
    """
    Create a heatmap of the correlation between all the parameters
    """
    matrice = data.corr()
    k = min(len(data.columns),10) # Nombre de variables à garder dans la HeatMap
    cols = matrice.nlargest(k,target)[target].index
    cm = np.corrcoef(data[cols].values.T)
    f, ax = plt.subplots(figsize=(10, 5))
    hm = sns.heatmap(cm, annot=True, square=True,linewidths=.5,annot_kws={'size': 9}, yticklabels=cols.values, xticklabels=cols.values)
    plt.show()