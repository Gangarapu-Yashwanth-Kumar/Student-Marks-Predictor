import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
# Ensure your model path is correct relative to where you run app.py
# If student_mark_predictor.pkl is in the same directory as app.py,
# you can simplify the path.
model = joblib.load(r"C:\Users\HP\A VS Code\Marks Predictor\student_mark_predictor.pkl")



df = pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    global df
    
    # Changed to int(x) to handle integer input
    input_features = [int(x) for x in request.form.values()]
    features_value = np.array(input_features)
    
    #validate input hours
    if input_features[0] < 0 or input_features[0] > 24:
        # Changed the error message to be more general as per previous instructions
        return render_template('index.html', prediction_text='Please enter valid hours between 0 to 24.')
        

    output = model.predict([features_value])[0][0].round(2)

    # input and predicted value store in df then save in csv file
    df= pd.concat([df,pd.DataFrame({'Study Hours':input_features,'Predicted Output':[output]})],ignore_index=True)
    print(df)   
    df.to_csv('smp_data_from_app.csv')

    return render_template('index.html', prediction_text='You will get [{}%] marks, when you do study [{}] hours per day '.format(output, features_value[0]))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
