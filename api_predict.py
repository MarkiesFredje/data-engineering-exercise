import os
from flask import Flask, jsonify
from flask_restful import reqparse
import numpy as np
from joblib import load

app = Flask(__name__)


@app.route('/prediction', methods=['GET'])
def prediction():
    """Script for reading the arguments and predicting the price"""
    path_model = os.path.join(os.getcwd(), 'lgbr_cars.model')
    lgbr_cars_model = load(path_model)
    parser = reqparse.RequestParser()
    parser.add_argument('vehicleType', required=True, type=int)
    parser.add_argument('gearBox', required=True, type=int)
    parser.add_argument('powerPS', required=True, type=int)
    parser.add_argument('model', required=True, type=int)
    parser.add_argument('kilometer', required=True, type=int)
    parser.add_argument('monthOfRegistration', required=True, type=int)
    parser.add_argument('fuelType', required=True, type=int)
    parser.add_argument('brand', required=True, type=int)
    args = parser.parse_args()
    vehicle_type = args['vehicleType']
    gear_box = args['gearBox']
    power_ps = args['powerps']
    model = args['model']
    kilometer = args['kilometer']
    month_of_registration = args['monthOfRegistration']
    fuel_type = args['fuelType']
    brand = args['brand']
    input_list = [vehicle_type, gear_box, power_ps, model,
                  kilometer, month_of_registration, fuel_type, brand]
    input_list = np.array(input_list, dtype=int)
    predicted_val = lgbr_cars_model.predict([input_list])[0]
    res = {'prediction': predicted_val}

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)



