import datetime as dt
from flask import Flask, request

from ie_bike_model.model import predict, train_and_persist
from ie_bike_model.model import read_data, preprocess, dummify, postprocess

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

    hour_train = read_data(hour_path)
    hour_train = preprocess(hour_train)
    hour_train = dummify(hour_train)
    hour_train = postprocess(hour_train)

    m_weathersit = hour_train["weathersit"].mean
    m_temperature_C = hour_train["temperature_C"].mean
    m_feeling_temperature_C = hour_train["feeling_temperature_C"].mean
    m_humidity = hour_train["humidity"].mean
    m_windspeed = hour_train["windspeed"].mean

    inicial_time = dt.datetime.now()

    parameters = dict(request.args)
    parameters["date"] = dt.datetime.fromisoformat(parameters["date"])
    parameters["weathersit"] = int(parameters.get("weathersit", m_weathersit))
    parameters["temperature_C"] = float(
        parameters.get("temperature_C", m_temperature_C)
    )
    parameters["feeling_temperature_C"] = float(
        parameters.get("feeling_temperature_C", m_feeling_temperature_C)
    )
    parameters["humidity"] = float(parameters.get("humidity", m_humidity))
    parameters["windspeed"] = float(parameters.get("windspeed", m_windspeed))

    model = parameters.get("model", "xgboost")

    result = predict(parameters, model=model)

    total_time = dt.datetime.now() - inicial_time

    return {"result": result, "time": total_time}
