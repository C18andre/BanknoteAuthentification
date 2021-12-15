from sklearn.model_selection import train_test_split

def split(data,target,test_size=0.2,train_size=0.8) :
    """
    X : numpy, data
    Y : numpy, target
    test_size : Float, representing the percentage of the test set
    """
    if target not in data.columns :
        raise ValueError
    Y = data[target]
    X = data.drop(target,axis=1)
    return train_test_split(X,Y,test_size=0.33)