import datetime as dt
from flask import Flask, request

from ie_bike_model.model import predict, train_and_persist

app = Flask(__name__)


@app.route("/Hello")
def hello():
    name = request.args.get("name", "World")
    return "Hello, " + name + "!"


@app.route("/training_score")
def get_score():
    algorithm = request.args.get("algorithm", "xgboost")
    score = train_and_persist(model=algorithm)

    return "Training Score for " + algorithm + "  =  " + score


@app.route("/predict")
def get_predict():

    inicial_time = dt.datetime.now()

    parameters = dict(request.args)
    parameters["date"] = dt.datetime.fromisoformat(parameters["date"])
    parameters["weathersit"] = int(parameters["weathersit"])
    parameters["temperature_C"] = float(parameters["temperature_C"])
    parameters["feeling_temperature_C"] = float(parameters["feeling_temperature_C"])
    parameters["humidity"] = float(parameters["humidity"])
    parameters["windspeed"] = float(parameters["windspeed"])

    model = parameters.get("model", "xgboost")

    result = predict(parameters, model=model)

    total_time = dt.datetime.now() - inicial_time

    return {"result": result, "time": total_time}
