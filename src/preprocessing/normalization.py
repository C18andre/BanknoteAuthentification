from sklearn.preprocessing import StandardScaler, MinMaxScaler

def normalization(data,features,mode=0):
    """
    Normalized the numerical features of the dataset

    data: dataframe
    features: list of feature to be normalized
    mode: 0:StandardScaler 1:MinMax
    
    """

    assert (mode==0) or (mode==1), "mode=0: Standard Scaler, mode=1 MinMaxScaler"

    if mode ==0:
        scaler = StandardScaler()
    else:
        scaler = MinMaxScaler()

    data[features] = scaler.fit_transform(data[features])
    return data