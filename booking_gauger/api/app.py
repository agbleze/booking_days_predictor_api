#%%
import joblib
import warnings
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from .helpers import predict_booking, get_path

warnings.filterwarnings('ignore')

model_path = get_path(folder_name='booking_gauger/api/model_store', file_name='best_model.model')
model = joblib.load(filename=model_path)

#%%
app = Flask(__name__)
api = Api(app)
class predictBookingDays(Resource):
    @staticmethod
    def post():
        user_input = request.get_json()
        num_sessions = user_input['num_sessions']
        city = user_input['city']
        country = user_input['country']
        device = user_input['device_class']
        instant_booking = user_input['instant_booking']
        user_verified = user_input['user_verified']
        prediction = predict_booking(model=model, 
                                     num_sessions=num_sessions, 
                                     city=city, 
                                     country=country,
                                     device_class=device, 
                                     instant_booking=instant_booking,
                                     user_verified=user_verified
                                     )
        prediction_json = {'predicted_value': prediction}
        return jsonify(prediction_json)
    
api.add_resource(predictBookingDays, '/predict')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
        


        
# %%
