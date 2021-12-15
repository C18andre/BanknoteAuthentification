from sklearn.preprocessing import LabelEncoder
from collections import defaultdict

def label_encoder(data) :
    """
    data : Data to label
    Return labellized data and the corresponding dictionnary
    """
    columns_to_label = data.select_dtypes(include="object").columns
    label_encoder_dico = defaultdict(LabelEncoder)
    if len(columns_to_label) == 0 :
        return data,{}
    for col in columns_to_label :
        print(col)
        #label_encoder_dico[col] = LabelEncoder()
        #label_encoder_dico[col].fit(data[col])

        #print(label_encoder_dico[col].fit_transform(data[col]))
        #data[col] = label_encoder_dico[col].fit_transform(data[col])
    return data,label_encoder_dico

