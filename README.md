# booking_days_predictor_api

## Project Description

This repo contains code for developing package for machine learning API for predicting number of days a client will book a room online for accommodation.

The machine learning model developed is served as an API which can be run locally or deployed into production. With this, requests can be made with appropriate parameters to the API to obtain predictions. 

Instead os running it as an API, modules are also provided in the package that can be imported and make prediction. Details of how the machine learning model was developed is 
available [here](https://github.com/agbleze/machine_learning_api).


## How to run the package

1. Create and activate a virtual enviornment. This can be done on MacOs as follows:

- I. Virtual environment called env (name it with your preference)

``` python -m venv env ```

- II. Activate the virtual environment

``` source env/bin/activate ```

2. Clone the repository as follows

```git clone https://github.com/agbleze/booking_days_predictor_api.git ```

3. Install the package as follows

``` pip install . ```

4. Run the package (By this the machine learning model is served as an API)

``` python -m booking_gauger ```

The expected output for this action is an the URL of the model is being served in your terminal. By default, the URL is expected to be http://192.168.0.168:8080  or http://127.0.0.1:8080. This is used as the default URL for testing the ML API endpoint.

5. Run test of the ML API endpoint

```pytest ```


## Tutorial: How to use the package

#### Make predictions of number of days the a room will be booked for accommodation online using the ML API

In order to utilize the ML API endpoint for prediction, it is nautural to first run the api endpoint following the procedures above. 

Predictions can be made by running some functions provided by package either in a jupyter notebook environment or as a python file.

Making a prediction with request to ML endpoint is undertaken as follows:

```python

from booking_gauger.api.helpers import request_prediction

in_data = {
 'num_sessions': 2,
 'city_encoded': 4,
 'country_encoded': 1,
 'device_class_encoded': 2,
 'instant_booking_encoded': 0,
 'user_verified_encoded': 1 
}

days_predicted = request_prediction(data=in_data)
round(days_predicted)
```

It is that simple! Details of what the various parameters or better still keys of the dictionary passed can be found in the documentation of the request_prediction function.


Actually, there is not much difference between the steps used to request a prediction from the API endpoint and that of making prediction with the model stored in the package.
It is just a matter of which function is being imported for use. 

In case, you have not run the package as an API endpoint as depicted above at step 4, then the next steps will serve you best. So without step 4 and 5, you can use the package for prediction right after installing it. Just follow suit.


### Predict number of booking days with ML package

In either jupyter notebook or python file, the steps for prediction are identified as follows;

```python
# import function for prediction
from booking_gauger.api.helpers import predict_booking

# Meaning of argments are found in the function documentation
predictions = predict_booking(num_sessions=2, city_encoded=4, country_encoded=1,
                                device_class_encoded=2, instant_booking_encoded=0, 
                                user_verified_encoded=1
                            )

predictions[0]
```






