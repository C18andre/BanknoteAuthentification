import numpy as np
import pandas as pd

def cleaner(settings) :
    """
    1. Clean the data and fill the missing values
    2. Then save it to bronze folder
    """
    banknote = pd.read_csv(settings["paths"]["banknote"].format("raw"))
    kidney = pd.read_csv(settings["paths"]["kidney"].format("raw"))
    
    print(banknote.head())
    print(kidney.head())




