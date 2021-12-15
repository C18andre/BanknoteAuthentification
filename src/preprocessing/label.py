from sklearn.preprocessing import OneHotEncoder
from collections import defaultdict

def label_encoder(data) :
    columns_to_label = data.select_dtypes(include="object").columns
    dico_le = defaultdict(OneHotEncoder)
    if len(columns_to_label) == 0 :
        return data
    for col in columns_to_label :
        le = OneHotEncoder()
        fit =
    data.apply(lambda x : )

