#%%
import joblib
import os
import requests
import json


# function to get the full pathname for the data file

def get_path(folder_name: str, file_name: str):
    cwd = os.getcwd()
    return f"{cwd}/{folder_name}/{file_name}"

DEFAULT_URL = "http://192.168.0.168:8080/predict"

#%%
model_path = get_path(folder_name='booking_gauger/api', 
                      file_name='model.model'
                    )
model = joblib.load(filename=model_path)

def predict_booking(num_sessions, city_encoded, country_encoded,
                    device_class_encoded, instant_booking_encoded,
                    user_verified_encoded, model=model
                    ):
    X = [num_sessions, city_encoded, country_encoded,
         device_class_encoded, instant_booking_encoded,
        user_verified_encoded
        ]
    if type(X) is not list:
        raise Exception('X must be a list')
    if len(X) != 6:
        raise Exception('X must contain 6 values for \
                        num_sessions, city, country, device, \
                        instant booking, user verified'
                        )
    prediction = model.predict([X])
    return prediction.tolist()


def request_prediction(data: dict, URL: str = DEFAULT_URL,) -> int:
    """
    This function makes an API request to the booking gauger API and return
    a prediction of number of days room will be booked for accommodation.

    Parameters
    ----------
    URL : Endpoint of booking gauger API
        The API link.
    data : dict
        input data to be used for prediction. This should be a dictionary
        with keys as num_sessions, city_encoded, country_encoded,
         device_class_encoded, instant_booking_encoded and user_verified_encoded

        num_sessions: is the number of sessions of an online client using platform 
                      for booking accommodation
        city_encoded: City from which client is accessing the online booking platform
        country_encoded: Country from which client is accessing the online booking platform
        device_class_encoded: Type of Device used by client to access the online booking platform
        instant_booking_encoded: Whether client used instant booking button for the booking
        user_verified_encoded: Whether the user is verified 
                      
    Returns
    -------
    int
        prediction.

    """
    req = requests.post(url=URL, json=data)
    response = req.content
    prediction = json.loads(response)['predicted_value'][0]
    return prediction
 
 