

#%%
#import requests
from booking_gauger.api.helpers import request_prediction, predict_booking
import warnings

warnings.filterwarnings("ignore")

# %%
#URL = "http://192.168.1.2:8080/predict"

URL = "http://192.168.0.168:8080/predict"

#in_data = {}

in_data = {
 'num_sessions': 2,
 'city_encoded': 4,
 'country_encoded': 1,
 'device_class_encoded': 2,
 'instant_booking_encoded': 0,
 'user_verified_encoded': 1 
}

def test_request_prediction():
    result = request_prediction(data=in_data)
    assert isinstance(result, float)
    
# %%

test_request_prediction()

# %%

predictions = predict_booking(num_sessions=2, city_encoded=4, country_encoded=1,
                device_class_encoded=2, instant_booking_encoded=0, 
                user_verified_encoded=1)


# %%
def test_predict_booking_is_list(num_sessions=2, city_encoded=4, 
                                 country_encoded=1,device_class_encoded=2, 
                                 instant_booking_encoded=0, 
                                user_verified_encoded=1
                                ):
    result = predict_booking(num_sessions=num_sessions, city_encoded=city_encoded,
                    country_encoded=country_encoded, device_class_encoded=device_class_encoded,
                    instant_booking_encoded=instant_booking_encoded,
                    user_verified_encoded=user_verified_encoded
                    )
    assert isinstance(result, list)
    
    
def test_predict_booking_value_is_float():
    result = predict_booking(num_sessions=2, city_encoded=4, 
                            country_encoded=1,device_class_encoded=2, 
                            instant_booking_encoded=0, 
                            user_verified_encoded=1
                            )
    value = result[0]
    assert isinstance(value, float)
    
    