from sklearn.model_selection import ShuffleSplit, train_test_split

def shuffle_split(n_splits,test_size=0.2,train_size=0.8) :
    """
    n_splits : Integer, number of splits
    test_size : Float, representing the percentage of the test set
    train_size : Float, representing the percentage of the train set
    return un shuffle split
    """
    cv = ShuffleSplit(n_splits=n_splits,test_size=test_size,train_size=train_size)
    return cv



def split(data,target,test_size=0.2,train_size=0.8) :
    """
    X : numpy, data
    Y : numpy, target
    test_size : Float, representing the percentage of the test set
    """
    if target not in data.columns :
        raise ValueError
    Y = data[target]
    X = data.drop(data[target])
    return train_test_split(X,Y,test_size=0.33)