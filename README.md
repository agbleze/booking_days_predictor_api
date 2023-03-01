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

``` source env/bin/activate ````

2. Clone the repository as follows

```git clone https://github.com/agbleze/booking_days_predictor_api.git ```

3. Install the package as follows

``` pip install . ```

4. Run the package (By this the machine learning model is served as an API)

``` python -m booking_gauger ```

The expected output for this action is an the URL of the model is being served in your terminal. By default, the URL is expected to be http://192.168.0.168:8080  or http://127.0.0.1:8080. This is used as the default URL for testing the ML API endpoint.

5. Run test of the ML API endpoint

```pytest ```








