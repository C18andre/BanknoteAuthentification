import numpy as np
from numpy.lib.function_base import average
from sklearn.model_selection import cross_val_score


def train_models(models,X_train,X_test,y_train,y_test,cv=5): #Alexandre
    """
    Train several model and return a report of their accuracies.
        perf_train: Performance of each model on train set
        perf_test: Performance of each model on test set

    models: Dict of models to train (sklearn models only)
    X_train: Training data (without target)
    X_test: Testing data (without target)
    y_train: Target of the training set
    y_test: Target of the testing set
    cv: cross validation folds
    """

    perf_train = {}
    perf_test = {}

    for name,m in models.items():

        scores = cross_val_score(m, X_train, y_train, cv=cv)
        perf_train[name] = [scores.mean(), scores.std()]

        perf_test[name] = m.score(X_test,y_test)
    
    return perf_train, perf_test





