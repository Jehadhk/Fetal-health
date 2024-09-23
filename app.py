from flask import Flask, render_template

app = Flask(__name__)

# Homepage route, which is biography.html
@app.route('/')
def home():
    return render_template('biography.html')  # Use biography.html as the homepage

# Explicit Biography route
@app.route('/biography')
def biography():
    return render_template('biography.html')  # Biography page

# Fetal Health Prediction page
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return render_template('prediction.html')  # Prediction page

# Resume page
@app.route('/resume')
def resume():
    return render_template('resume.html')  # Resume page

# General Projects page (if you want to add this later)
@app.route('/projects')
def projects():
    return render_template('projects.html')  # General Projects page

if __name__ == '__main__':
    app.run(debug=True, port=5011)
