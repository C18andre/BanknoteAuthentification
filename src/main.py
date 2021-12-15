## Main 
import json
with open("src/settings.json") as file:
            settings = json.load(file)

 ############################################ Imports ############################################
import pandas as pd
from preprocessing.cleaner import convert_cat_to_num,missing_value
from preprocessing.test import test as p_test
from preprocessing.label import label_encoder


############################################ Pipeline ############################################
# Preprocessing
data = pd.read_csv(settings["paths"]["banknote"])
clean_data = missing_value(data)
p_test(clean_data,data)
label_data,label_dico = label_encoder(data)


# Models


# Visualisation
