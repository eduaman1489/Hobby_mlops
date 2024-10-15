import json
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('regmodel.pkl','rb'))

@app.route('/make_api_call',methods=['POST'])
def predict_api():
    try:
        data=request.json['data']
        print('raw data :', data)
        new_data = np.array(data)#.reshape(1, -1)
        print('reshaped data :', new_data)
        output = model.predict(new_data)
        return jsonify({"prediction": output.tolist()})  # Convert to list for JSON serialization
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Return error message

if __name__=="__main__":
    app.run(debug=True) # app.run(threaded=True) to make it Multi-threaded, otherwise its single-threaded
   