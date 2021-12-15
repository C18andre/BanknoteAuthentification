## Main 
######################################## HyperParameters ########################################
TARGET_NAME = "class"
DATA_NAME = "kidney"
# DATA_NAME = "banknote"
FEATURES = ["id","age","bp","sg","al","su","bgr","bu","sc","sod","pot","hemo","pcv","wc","rc"]
# FEATURES = ["variance","skewness","curtosis","entropy"]
import json
with open("src/settings.json") as file:
            settings = json.load(file) # Retrieve paths 

############################################ Imports ############################################
import pandas as pd
from preprocessing.cleaner import convert_cat_to_num,missing_value
from preprocessing.test import test as p_test
from preprocessing.label import label_encoder
from preprocessing.split import split
from visualization.maps import heatmap

############################################ Pipeline ############################################
# Preprocessing
data = pd.read_csv(settings["paths"][DATA_NAME])                    # Read the csv file
clean_data_1 = convert_cat_to_num(data,FEATURES)                    # Convert object datatype to float when its possible
clean_data_2 = missing_value(clean_data_1,drop_num=True)            # Fill the missing values
p_test(clean_data_2,data)                                           # Test the length of data after cleaning process
label_data,label_dico = label_encoder(clean_data_2)                 # Encode strings data
X_train, X_test, y_train, y_test = split(label_data,TARGET_NAME)

# Vizualisation
heatmap(clean_data_2,TARGET_NAME)

# Models


# Visualisation
