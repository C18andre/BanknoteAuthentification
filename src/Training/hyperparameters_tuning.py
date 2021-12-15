from sklearn.model_selection import GridSearchCV


def hyperparameters_tuning(model,params,X_train,y_train,cv=5): #Alexandre
    """
    Perform Grid Search Cv on a model regarding the provided list of parameters
        return a dict with the scores of each combination

    model: sklearn model
    params: dict of parameters
    X_train: Training features
    y_train: Target
    cv: number of cross-fold
    """
    logs_grid = {}

    grid = GridSearchCV(model, params,cv=cv)
    grid.fit(X_train,y_train)

    print("Best combination of parameters is :",grid.best_params_)
    for i,p in enumerate(grid.cv_results_["params"]):
        logs_grid[str(p)] = grid.cv_results_["mean_test_score"][i]
    return logs_grid, grid.best_estimator_