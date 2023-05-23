from flask import Flask, render_template, request
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)

# Laden des trainierten Machine Learning-Modells
model = joblib.load("flight_delay_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Extrahieren der Eingabedaten aus dem POST-Request
    airline = request.form["airline"]
    time = request.form["time"]
    airport_from = request.form["airport_from"]
    airport_to = request.form["airport_to"]
    day_of_week = request.form["day_of_week"]

    # Erstellen eines DataFrame mit den eingegebenen Daten
    data = pd.DataFrame(
        [[airline, time, airport_from, airport_to, day_of_week]],
        columns=["Airline", "Time", "AirportFrom", "AirportTo", "DayOfWeek"],
    )

    # Vorhersage des Flugverspätungsstatus
    prediction = model.predict(data)[0]

    # Rendern des Ergebnisses auf der Ergebnisseite
    return render_template("result.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
