
def test(data,clean_data) :
    """
    Test between clean data and data
    """
    assert len(clean_data)>0.9*len(data)
    assert max(clean_data.isnull().sum(axis=0)) < 0.1*len(data)
    