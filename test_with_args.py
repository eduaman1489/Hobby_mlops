import json
import numpy as np
import joblib
import sys

def init():
    global model #  Available throughout the entire script, not just inside the init() function.
    model_path = "regmodel.pkl" 
    model = joblib.load(model_path)

def run_model(raw_data):
    try:
        data = json.loads(raw_data)['data']
        data = np.array(data)
        result = model.predict(data)
        return {"Prediction": result .tolist()}
    except Exception as e:
        result = str(e)
        return {"Error": result} # {'Error': 'X has 9 features, but Ridge is expecting 10 features as input.'}

if __name__ == "__main__":
    init()  # Initialize the model as global
    if len(sys.argv) != 2: # if the number of arguments passed to the script is not equal to 2 , one is file and and other is input test data 
        print("Run the script with 2 parameters. One is file itself and second is the input data: python test.py '{\"data\": [[...], [...]]}'")
        sys.exit(1)

    input_data = sys.argv[1]
    prediction = run_model(input_data)
    print(prediction)

# python test.py "{\"data\": [[0.03807590643330433, 0.0506801187398187, 0.06169620651868896, 0.0218770970572096, -0.04422349927884412, -0.03482076576132779, -0.04340076571505772, -0.002592261668673879, 0.01990652419037737, -0.01764613053217129]]}"