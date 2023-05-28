from predict import predict_delay
from flask import Flask, render_template, request, jsonify
import os
import pandas as pd

app = Flask(__name__, template_folder="frontend", static_folder="static")

class TimeCalculator:
    @staticmethod
    def calculate_time_in_minutes(hours, minutes):
        return hours * 60 + minutes

class WeekdaySelection:
    weekdays = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7
    }

    def __init__(self):
        self.selected_weekday = None

    def get_weekday_options(self):
        return self.weekdays.keys()

    def set_selected_weekday(self, weekday):
        self.selected_weekday = self.weekdays.get(weekday)  # Get the numeric representation

    def get_selected_weekday(self):
        return self.selected_weekday
    
# Read the airlines_delay_cleaned_unique_airline.csv file
df_airlines = pd.read_csv('../data/airlines_delay_cleaned_unique_airline.csv')
df_airports = pd.read_csv('../data/airlines_delay_cleaned_unique_airport.csv')

df_airlines.sort_values(by=['Airline'], inplace=True)
df_airports.sort_values(by=['Airport'], inplace=True)

@app.route("/")
def home():
    # Get the unique airlines from the DataFrame
    unique_airlines = df_airlines['Airline']
    unique_airports = df_airports['Airport']

    weekday_selection = WeekdaySelection()
    weekday_options = weekday_selection.get_weekday_options()

    return render_template("index.html", airlines=unique_airlines, airports=unique_airports, weekday_options=weekday_options)


@app.route("/predict", methods=["POST"])
def predict():
    # Extract hours and minutes from the selected time
    time = request.form['time']
    hours, minutes = map(int, time.split(':'))

    # Calculate the departure time in minutes
    time_calculator = TimeCalculator()
    departure_time_in_minutes = time_calculator.calculate_time_in_minutes(hours, minutes)

    # Get the user inputs from the request and assign the calculated departure time
    weekday_selection = WeekdaySelection()
    weekday_selection.set_selected_weekday(request.form['day_of_week'])

    predict_delay(departure_time_in_minutes,request.form['length'],request.form['airline'],request.form['airport_from'],request.form['airport_to'],weekday_selection.get_selected_weekday())

    prediction_result = predict_delay(departure_time_in_minutes, request.form['length'], request.form['airline'],
                                      request.form['airport_from'], request.form['airport_to'],
                                      weekday_selection.get_selected_weekday())

    return jsonify(result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)
