CGPA Prediction using Machine Learning & Flask

This project predicts the expected package based on a student's CGPA using a Machine Learning model.
The trained model is integrated into a Flask backend with an HTML frontend to make predictions in real time.

Features

Predicts package based on CGPA

Uses a trained Machine Learning model

Integrated Flask API for predictions

HTML/CSS frontend for user interaction

Clean and well-structured code

Tech Stack

Python (3.10 or above)

Flask – Backend framework

scikit-learn – Machine Learning model training

Pandas & NumPy – Data processing

HTML / CSS – Frontend

Pickle – Saving and loading the trained model

Project Structure
CGPA_Prediction/
│── dataset.csv          # Dataset used for training (optional)
│── package.pkl          # Trained ML model
│── main.py              # Flask backend
│── templates/
│    └── home.html       # Frontend HTML page
│── static/
│    └── style.css       # (Optional) Styling for HTML
│── requirements.txt     # Project dependencies
│── README.md            # Project documentation

Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/cgpa-prediction.git
cd cgpa-prediction

2. Create a Virtual Environment
python -m venv .venv

3. Activate the Environment

For Windows:

.venv\Scripts\activate


For Mac/Linux:

source .venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Run the Flask App
python main.py

6. Open the App in Browser
http://127.0.0.1:5000/

Machine Learning Model

Algorithm Used: Linear Regression (or the one you used)

Training Data: dataset.csv

Model File: package.pkl

How to Load the Model:

import pickle

model = pickle.load(open('package.pkl', 'rb'))
prediction = model.predict([[8.2]])
print(prediction)

Usage

Enter your CGPA in the input field.

Click on Predict.

Get the predicted package instantly.

Requirements

requirements.txt should include:

flask
pandas
numpy
scikit-learn


Install all dependencies:

pip install -r requirements.txt

License

This project is open-source and available under the MIT License.
