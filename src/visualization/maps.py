import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def Nan_map(data):
    """
    return a figure to detect the Nan values
    """
    plt.figure(figsize=(20,10))
    sns.heatmap(data.isna(),cbar=False)
    plt.show()


def heatmap(data,target) :
    """
    Create a heatmap of the correlation between all the parameters
    """
    matrice = data.corr()
    k = 10 # Nombre de variables à garder dans la HeatMap
    cols = matrice.nlargest(k,target)[target].index
    cm = np.corrcoef(data[cols].values.T)
    f, ax = plt.subplots(figsize=(12, 6))
    hm = sns.heatmap(cm, annot=True, square=True,annot_kws={'size': 9}, yticklabels=cols.values, xticklabels=cols.values)
    plt.show()