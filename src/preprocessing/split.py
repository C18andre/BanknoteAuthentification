from sklearn.model_selection import ShuffleSplit, train_test_split

def shuffle_split(data,n_splits,test_size=0.2,train_size=0.8) :
    """
    data : Pandas dataframe
    n_splits : Integer, number of splits
    test_size : Float, representing the percentage of the test set
    train_size : Float, representing the percentage of the train set
    return un shuffle split
    """
    cv = ShuffleSplit(n_splits=n_splits,test_size=test_size,train_size=train_size)
    return cv



def split(X,Y,test_size=0.2,train_size=0.8) :
    """
    X : numpy, data
    Y : numpy, target
    test_size : Float, representing the percentage of the test set
    """
    return train_test_split(X,Y,test_size=0.33)