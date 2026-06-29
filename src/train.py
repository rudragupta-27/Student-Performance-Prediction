import joblib
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from src.data_preprocessing import create_preprocessor
def train_model(data_path):
    """
    Train the final Random Forest model and save it.
    """

    df = pd.read_csv(data_path)
    X = df.drop("math score", axis=1)
    y = df["math score"]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    preprocessor = create_preprocessor(X_train)
    X_train_processed = preprocessor.fit_transform(X_train)
    param_grid = {"n_estimators": [50, 100, 200],"max_depth": [None, 5, 10, 20]}
    grid_search = GridSearchCV(RandomForestRegressor(random_state=42),param_grid=param_grid,cv=5,scoring="r2",n_jobs=-1)
    grid_search.fit(X_train_processed, y_train)
    joblib.dump(grid_search.best_estimator_, "models/model.pkl")
    joblib.dump(preprocessor, "models/preprocessor.pkl")
    return grid_search.best_estimator_