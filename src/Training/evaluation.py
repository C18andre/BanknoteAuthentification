from sklearn.metrics import f1_score, confusion_matrix, classification_report


def cla_evaluation(model,X_test,y_test): #Alexandre
    """
    For a classification problem, return classic performance indicators

    model: model to assess
    X_test: Testing set
    y_test: target on test set
    """


    y_pred = model.predict(X_test)
    
    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))
    