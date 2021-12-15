## Main 
import json
with open("src/settings.json") as file:
            settings = json.load(file)

######################################## HyperParameters ########################################
CLASS_NAME = "class"
DATA_NAME = "banknote"

############################################ Imports ############################################
import pandas as pd
from preprocessing.cleaner import convert_cat_to_num,missing_value
from preprocessing.test import test as p_test
from preprocessing.label import label_encoder
from preprocessing.split import split

############################################ Pipeline ############################################
# Preprocessing
data = pd.read_csv(settings["paths"][DATA_NAME])
clean_data = missing_value(data)
p_test(clean_data,data)
label_data,label_dico = label_encoder(data)
X_train, X_test, y_train, y_test = split(data,CLASS_NAME)

# Models


# Visualisation
