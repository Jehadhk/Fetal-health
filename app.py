from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from form
    features = [
        float(request.form['baseline_value']),
        float(request.form['accelerations']),
        float(request.form['fetal_movement']),
        float(request.form['uterine_contractions']),
        float(request.form['light_decelerations']),
        float(request.form['severe_decelerations']),
        float(request.form['prolongued_decelerations']),
        float(request.form['abnormal_short_term_variability']),
        float(request.form['mean_value_of_short_term_variability']),
        float(request.form['percentage_of_time_with_abnormal_long_term_variability']),
        float(request.form['mean_value_of_long_term_variability']),
        float(request.form['histogram_width']),
        float(request.form['histogram_min']),
        float(request.form['histogram_max']),
        float(request.form['histogram_number_of_peaks']),
        float(request.form['histogram_number_of_zeroes']),
        float(request.form['histogram_mode']),
        float(request.form['histogram_mean']),
        float(request.form['histogram_median']),
        float(request.form['histogram_variance']),
        float(request.form['histogram_tendency']),
    ]
    
    # Convert features to a NumPy array and make prediction
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)[0]

    # Print prediction for debugging
    print("Prediction:", prediction)
    
    # Render the result on the HTML page
    return render_template('index.html', prediction=f'Predicted Fetal Health Status: {prediction}')

if __name__ == '__main__':
    app.run(debug=True)
