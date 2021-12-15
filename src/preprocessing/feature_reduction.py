from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def PCA_feature_reduction(data,variance=0.95): #Alexandre
    """
    Readuce the feature space and keep the desierde variability in data
    data: dataframe
    variance : float in [0,1]
    """
    pca = PCA(n_components = variance)
    X_reduced = pca.fit_transform(data)
    
    return X_reduced

def plot_2D(data,target): #Alexandre
    """
    Use PCA to plot the data in 2D
    data:dataframe
    target:target
    """
    pca = PCA(n_components = 2)
    X2D = pca.fit_transform(data)

    plt.figure(figsize=(13,10))
    plt.scatter(X2D[:, 0], X2D[:, 1], c=target, cmap="jet")
    plt.axis('off')
    plt.colorbar()
    plt.show()

