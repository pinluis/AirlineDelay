from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='frontend')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Simulieren der Vorhersage des Flugverspätungsstatus (immer True)
    prediction = True

    # Rendern des Ergebnisses auf der Ergebnisseite
    return render_template("result.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
