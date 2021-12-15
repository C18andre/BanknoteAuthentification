from sklearn.model_selection import GridSearchCV


def hyperparameters_tuning(model,params,X_train,y_train,cv=5):
    """
    Perform Grid Search Cv on a model regarding the provided list of parameters
        return a dict with the scores of each combination

    model: sklearn model
    params: dict of parameters
    X_train: Training features
    y_train: Target
    cv: number of cross-fold
    """


    grid = GridSearchCV(model, params,cv=cv)
    grid.fit(X_train,y_train)

    print(grid.best_params_)

    return grid.cv_results_['mean_test_score'], grid.best_estimator_