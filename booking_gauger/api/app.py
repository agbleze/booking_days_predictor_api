#%%
import joblib
import warnings
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from helpers import predict_booking, get_path

warnings.filterwarnings('ignore')

model_path = get_path(folder_name='booking_gauger/api', file_name='model.model')
model = joblib.load(filename=model_path)

#%%
app = Flask(__name__)
api = Api(app)
class predictBookingDays(Resource):
    @staticmethod
    def post():
        user_input = request.get_json()
        num_sessions = user_input['num_sessions']
        city = user_input['city_encoded']
        country = user_input['country_encoded']
        device = user_input['device_class_encoded']
        instant_booking = user_input['instant_booking_encoded']
        user_verified = user_input['user_verified_encoded']
        
        # data = X=[num_sessions, 
        #           city, 
        #           country,
        #           device, 
        #           instant_booking,
        #           user_verified
        #         ]
        prediction = predict_booking(model=model, 
                                     num_sessions=num_sessions, 
                                     city_encoded=city, 
                                     country_encoded=country,
                                     device_class_encoded=device, 
                                     instant_booking_encoded=instant_booking,
                                     user_verified_encoded=user_verified
                                     )
        prediction_json = {'predicted_value': prediction}
        return jsonify(prediction_json)
    
api.add_resource(predictBookingDays, '/predict')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
        
        
# %%
