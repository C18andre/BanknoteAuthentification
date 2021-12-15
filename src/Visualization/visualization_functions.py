import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def Nan_map(data):
    """
    return a figure to detect the Nan values
    """
    plt.figure(figsize=(20,10))
    sns.heatmap(data.isna(),cbar=False)
    plt.show()

