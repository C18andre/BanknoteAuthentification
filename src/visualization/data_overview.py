import seaborn as sns
import matplotlib.pyplot as plt

def numeric_features_distribution(data,features,bandwith=1):
    """
    Use kde algorithm to plot the distribution of the numerical features

    data: dataframe
    bandwith: spread of kernel function
    """
    cols = 2
    rows = len(features)//2 +1
    plt.figure(figsize=(12,10))
    plt.subplots_adjust(right=1, top=1)
    for i,f in enumerate(features):
        plt.subplot(rows,cols,i+1)
        plt.title(f)
        sns.kdeplot(data[f],bw=bandwith)

def categorical_features_histograms(data,features):
    """
    Use kde algorithm to plot the distribution of the numerical features

    data: dataframe
    """
    cols = 2
    rows = len(features)//2 +1
    plt.figure(figsize=(12,10))
    plt.subplots_adjust(right=1, top=1)
    for i,f in enumerate(features):
        plt.subplot(rows,cols,i+1)
        plt.title(f)
        sns.countplot(x=f,data=data)
        
def numeric_features_distribution_per_class(data,features,target_column,bandwith=1):
    """
    Use kde algorithm to plot the distribution of the numerical features

    data: dataframe
    target_column: name of the targeted column
    bandwith: spread of kernel function
    """
    classes = data[target_column].unique()
    
    tmp_df = {}
    for c in classes:
        tmp_df[c] = data[data[target_column]==c]



    cols = 2
    rows = len(features)//2 +1
    plt.figure(figsize=(12,10))
    plt.subplots_adjust(right=1, top=1.5)
    for i,f in enumerate(features):
        plt.subplot(rows,cols,i+1)
        plt.title(f)
        for c,df in tmp_df.items():
            sns.kdeplot(df[f],bw=bandwith,label=c)
        plt.legend()

