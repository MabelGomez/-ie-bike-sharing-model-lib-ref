# Bike sharing prediction model
# Mabel Gomez
## Usage


Before running the application app.py is necessary to install the librery ie_bike_model.
To install the library:

```
$ pip install .
```

This library can be also run using without the app.
This implementation can be performed using two algorithms: Ridge (model = "rigde") and Xgboost (model = "xgboost")
In git:

```python
>>> import datetime as dt
>>> from ie_bike_model.model import train_and_persist, predict
>>> train_and_persist(model = "ridge") 
>>> predict({
...     "date": dt.datetime(2011, 1, 1, 0, 0, 0),
...     "weathersit": 1,
...     "temperature_C": 9.84,
...     "feeling_temperature_C": 14.395,
...     "humidity": 81.0,
...     "windspeed": 0.0,
... }, model = "ridge")
1
```

To run the app:

```python
>>> flask run
```

To get the trainning R-squared of the model, model=ridge or model=xgboost, if leave empty a Xgboost would be performed

```
http://127.0.0.1:5000/training_score?model=ridge
```

To get the predictions, model=ridge or model=xgboost, if leave empty a Xgboost would be performed

```
http://127.0.0.1:5000/predict?date=2012-10-01T18:00:00&weathersit=1&temperature_C=15&feeling_temperature_C=14&humidity=20&windspeed=5
```


## Development

To install a development version of the library:

```
$ flit install --symlink --extras=dev
```

To run the tests:

```
$ pytest
```

To measure the coverage:

```
$ pytest --cov=ie_bike_model
```

## Trivia

Total implementation time: **4 hours 30 minutes** 🏁
