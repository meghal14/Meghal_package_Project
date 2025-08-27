from flask import Flask, render_template, request
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("prediction.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    cgpa = float(request.form["cgpa"])
    prediction = float(model.predict(np.array([[cgpa]]))[0])
    return render_template("home.html", prediction_text=f"Predicted Package: {prediction:.2f} LPA")

if __name__ == "__main__":
    app.run(debug=True)

