import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# This function can be used to preprocess the data in the Jupyter Notebooks. This way we can keep the notebooks clean and our code DRY.
# It takes a dataframe as input and returns the preprocessed data as four separate variables: X_train, X_test, y_train, y_test.
def preprocess_data(df):
    # Separate features and target
    X = df.drop("Delayed", axis=1)
    y = df["Delayed"]

    # Define preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), ["Time", "Length"]),
            (
                "cat",
                OneHotEncoder(),
                ["Airline", "AirportFrom", "AirportTo", "DayOfWeek"],
            ),
        ]
    )

    # Fit and transform the features
    X_transformed = preprocessor.fit_transform(X)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X_transformed, y, test_size=0.2, random_state=17
    )

    return X_train, X_test, y_train, y_test
