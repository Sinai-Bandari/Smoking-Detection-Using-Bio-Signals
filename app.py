from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Initialize Flask application
app = Flask(__name__)
model=pickle.load(open(r"C:\Users\BLESSINA\OneDrive\Documents\Mini_project\miniproject\mini_project\mini_project\smoking_model","rb"))
# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict_form():
    return render_template('index.html')

@app.route('/output', methods=['POST'])
def output():
        # Parse input data from form
        ID = float(request.form.get('ID'))
        Gender = float(request.form.get('gender'))
        Age = float(request.form.get('age'))
        Height = float(request.form.get('height(cm)'))
        Weight = float(request.form.get('weight(kg)'))
        Waist = float(request.form.get('waist(cm)'))
        Eyesight_left = float(request.form.get('eyesight(left)'))
        Eyesight_right = float(request.form.get('eyesight(right)'))
        Hearing_left = float(request.form.get('hearing(left)'))
        Hearing_right = float(request.form.get('hearing(right)'))
        Systolic = float(request.form.get('systolic'))
        Relaxation = float(request.form.get('relaxation'))
        Fasting_blood_sugar = float(request.form.get('fasting_blood_sugar'))
        Cholesterol = float(request.form.get('Cholesterol'))
        Triglyceride = float(request.form.get('triglyceride'))
        HDL = float(request.form.get('HDL'))
        LDL = float(request.form.get('LDL'))
        Hemoglobin = float(request.form.get('hemoglobin'))
        Urine_protein = float(request.form.get('Urine_protein'))
        Serum_creatinine = float(request.form.get('serum_creatinine'))
        AST = float(request.form.get('AST'))
        ALT = float(request.form.get('ALT'))
        Gtp = float(request.form.get('Gtp'))
        Oral = float(request.form.get('oral'))
        Dental_caries = float(request.form.get('dental_caries'))
        Tartar = float(request.form.get('tartar'))

        # Combine inputs into a single array
        input_data = np.array([[ID, Gender, Age, Height, Weight, Waist, Eyesight_left, Eyesight_right,
                                Hearing_left, Hearing_right, Systolic, Relaxation, Fasting_blood_sugar,
                                Cholesterol, Triglyceride, HDL, LDL, Hemoglobin, Urine_protein,
                                Serum_creatinine, AST, ALT, Gtp, Oral, Dental_caries, Tartar]])
        data= pd.DataFrame(input_data,columns=['ID','gender','age','height(cm)','weight(kg)','waist(cm)','eyesight(left)','eyesight(right)',
                                                'hearing(left)','hearing(right)','systolic','relaxation','fasting_blood_sugar','Cholesterol',
                                                'triglyceride','HDL','LDL','hemoglobin','Urine_protein','serum_creatinine','AST','ALT',
                                                'Gtp','oral','dental_caries','tartar'])
        # Scale the input data
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)


        # Make prediction
        prediction = model.predict(scaled_data)

        # Render appropriate result page
        if prediction[0]==1:
            return render_template('precautions.html', pred="Smoker")
        else:
            return render_template('smoke_predict.html', pred="Non-Smoker")
        
    
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
