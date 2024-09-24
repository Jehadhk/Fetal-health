from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your model
model = pickle.load(open('model.pkl', 'rb'))

# Homepage route (biography.html)
@app.route('/')
def home():
    return render_template('biography.html')  # Use biography.html as the homepage

# Biography page route
@app.route('/biography')
def biography():
    return render_template('biography.html')  # Biography page

# Fetal Health Prediction page route
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    prediction_result = None  # Default value for prediction result

    if request.method == 'POST':
        # Get form data and convert to float
        form_data = [
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
            float(request.form['histogram_tendency'])
        ]

        # Make prediction using the model
        prediction_result = model.predict([form_data])[0]

    return render_template('prediction.html', prediction=prediction_result)  # Pass prediction to the template

# Resume page route
@app.route('/resume')
def resume():
    return render_template('resume.html')  # Resume page

# General Projects page route
@app.route('/projects')
def projects():
    return render_template('projects.html')  # General Projects page

if __name__ == '__main__':
    app.run(debug=True, port=5012)
