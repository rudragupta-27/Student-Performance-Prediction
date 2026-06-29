from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
def create_preprocessor(X):
    """
    Creates a preprocessing pipeline for the dataset.

    Parameters:
        X (DataFrame): Feature dataframe

    Returns:
        ColumnTransformer: Configured preprocessing pipeline
    """
    categorical_features = X.select_dtypes(include="object").columns
    numerical_features = X.select_dtypes(exclude="object").columns

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_features),
            ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_features),
        ]
    )
    return preprocessor