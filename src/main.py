## Main 
import json
with open("src/settings.json") as file:
            settings = json.load(file)
    
import pandas as pd
from preprocessing.cleaner import cleaner

data = pd.read_csv(settings["paths"]["banknote"])

