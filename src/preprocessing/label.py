from sklearn.preprocessing import LabelEncoder
from collections import defaultdict

def label_encoder(data) :
    """
    data : Data to label
    Return labellized data and the corresponding dictionnary
    """
    columns_to_label = data.select_dtypes(include="object").columns
    dico_le = defaultdict(LabelEncoder)
    if len(columns_to_label) == 0 :
        return data,{}
    for col in columns_to_label :
        data[col] = dico_le[col].fit_transform(data[col])
    return data,dico_le

