from flask import Blueprint, render_template, request, session
import joblib
import os

# Set up a Blueprint
main = Blueprint('main', __name__)

# Load the model
model_path = 'model/flu_predictor.pkl'
model = joblib.load(model_path) if os.path.exists(model_path) else None

# Initialize predictions in session
@main.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if 'predictions' not in session:
        session['predictions'] = []

    if request.method == "POST" and model:
        # Get form data
        temp = float(request.form.get("temperature"))
        humidity = float(request.form.get("humidity"))
        pop_density = float(request.form.get("population_density"))

        # Predict using the model
        prediction = model.predict([[temp, humidity, pop_density]])[0]

        # Store prediction in session
        session['predictions'].append({
            'temperature': temp,
            'humidity': humidity,
            'population_density': pop_density,
            'flu_cases': prediction
        })

    return render_template("predict.html", prediction=prediction, predictions=session['predictions'])
