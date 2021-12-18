from flask import Flask
import simplejson as json
from forecast import Forecast

# the main page of the API that calls all the values
app = Flask(__name__)


@app.route('/')
def main():
    return "Welcome, see README for information on how to run the API"


@app.route('/all_temp')
def all_temp():
    # the latest forecast for each location for every day
    response = json.dumps([row.toJson() for row in Forecast.selectAllTemp()])
    return response


@app.route('/the_temp')
def the_temp():
    # the average the_temp of the last 3 forecasts for each location for every day
    response = json.dumps(Forecast.selectThe_Temp())
    return response


@app.route('/top/<n>')
def top_metric(n):
    # Get the top n locations based on each available metric where n is a parameter given to the API call
    response = json.dumps(Forecast.selectTopMetric(n))
    return response


if __name__ == "__main__":
    app.run(debug=True)
