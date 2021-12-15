

def results_displayer(logs) :
    """
    Display the results of the tran/test process for each algorithm chosen
    Return graphs
    """
    if len(logs) == 0 :
        return "No data found"
    for model in logs :

