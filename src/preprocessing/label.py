from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from collections import defaultdict

def label_encoder(data) : #Clément
    """
    data : Data to label
    Return labellized data and the corresponding dictionnary
    """
    columns_to_label = data.select_dtypes(include="object").columns
    label_encoder_dico = defaultdict(LabelEncoder)
    if len(columns_to_label) == 0 :
        return data,{}
    for col in columns_to_label :
        label_encoder_dico[col].fit(data[col])
        data[col] = label_encoder_dico[col].transform(data[col])
    return data,label_encoder_dico

