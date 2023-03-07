

#%%
#import requests
from booking_gauger.api.helpers import request_prediction, predict_booking
import warnings

warnings.filterwarnings("ignore")

# %%
#URL = "http://192.168.1.2:8080/predict"

URL = "http://192.168.0.168:8080/predict"

#in_data = {}

in_data = {'num_sessions': 2, 'city': 'Berlin', 'country': 'DE',
            'device_class': 'desktop', 'instant_booking': 'Not_instant',
            'user_verified': 'Verified'
        }

def test_request_prediction():
    result = request_prediction(data=in_data)
    assert isinstance(result, float)
    
# %%

test_request_prediction()

# %%

predictions = predict_booking(device_class='desktop', city='Berlin', 
                            country='DE', instant_booking='Not_instant', 
                            user_verified='Verified', num_sessions=2
                            )


# %%
def test_predict_booking_is_list(device_class='desktop', city='Berlin', 
                                country='DE', instant_booking='Not_instant', 
                                user_verified='Verified', num_sessions=2
                                ):
    result = predict_booking(num_sessions=num_sessions, city=city,
                            country=country, device_class=device_class,
                            instant_booking=instant_booking,
                            user_verified=user_verified
                            )
    assert isinstance(result, list)
    
    
def test_predict_booking_value_is_float():
    result = predict_booking(device_class='desktop', city='Berlin', 
                            country='DE', instant_booking='Not_instant', 
                            user_verified='Verified', num_sessions=2
                            )
    value = result[0]
    assert isinstance(value, float)
    
    