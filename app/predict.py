import pickle
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def predict_delay(time, length, airline, airport_from, airport_to, day_of_week):
    # Load the model
    with open('../Models/logistic_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Create a new observation as a dictionary
    new_observation = {
        'Time': time,
        'Length': length,
        'Airline': airline,
        'AirportFrom': airport_from,
        'AirportTo': airport_to,
        'DayOfWeek': day_of_week,
    }

    # Convert the dictionary to a DataFrame
    new_observation_df = pd.DataFrame([new_observation])

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

    # Load training data and fit preprocessor
    X_train = pd.read_csv('../data/airlines_delay_cleaned.csv')
    preprocessor.fit(X_train)

    # Apply preprocessing to your new observation
    new_observation_df = preprocessor.transform(new_observation_df)

    # Use the model to predict whether the flight will be delayed
    prediction = model.predict(new_observation_df)

    if prediction[0] == 1:
        return "The flight is predicted to be delayed."
    else:
        return "The flight is predicted to be on time."
