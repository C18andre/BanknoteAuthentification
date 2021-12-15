import numpy as np
import pandas as pd


def convert_cat_to_num(data,features): #Alexandre
    """
    data: pandas dataframe
    features: the categorical features that we want to convert in numeric features
    """
    def go_float(x):
        try:
            return np.float(x)
        except:
            return np.nan
    for f in features:
        data[f] = data[f].apply(go_float)
        data[f] = data[f].astype(float)
    return data


def missing_value(data,num_function="mean",cat_function="Unknown",drop_cat=False,drop_num=False): #Alexandre/Clément
    """
    data: pandas dataframe
    num_function: function to apply for replacing "NaN" in numerical columns
    cat_function: function to apply for replacing "NaN" in categorical columns
    boolean drop_cat: if True, drop the rows with missing value in categorical features
    boolean drop_num : if True, drop the rows with missing value in numerical features
    """
    if "id" in data.columns:
        data.drop("id",axis=1,inplace=True)
    # Création de la fonction num
    if num_function == "mean" :
        num_function = np.mean
    if num_function == "min" :
        num_function= np.min
    else :
        num_function = np.mean
    
    num_f = data.select_dtypes(exclude="object").columns
    cat_f = data.select_dtypes(include="object").columns
    
    if drop_num:
        data.dropna(subset=num_f,inplace=True)
    else:
        data[num_f] = data[num_f].fillna(num_function)
    
    if drop_cat:
        data.dropna(subset=cat_f,inplace=True)
    else:
        data[cat_f] = data[cat_f].fillna(cat_function)
    return data






