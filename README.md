# data-engineering-exercise
Data engineering home exercise

To Run the flask api Application 
- pip -install Requirements.txt
- Download the model file in the same directory where the api file is located
- run python api_predict.py
- go to postman request with below details
    - method GET
    - Body
        - {
                "vehicleType": 3,
                "gearBox": 1,
                "powerPS": 190,
                "model": -1,
                "kilometer": 125000,
                "monthOfRegistration": 5,
                "fuelType": 3,
                "brand": 1
           }
    - Click on Send you should be able to get the predicted value