# import flask as Flask

from flask import Flask, render_template, request
from flask.wrappers import Request
import joblib
from sklearn.linear_model import LinearRegression


app = Flask(__name__)

model = joblib.load('hiring_model.pkl')

@app.route('/')
def welcome():
    return render_template('base.html')

@app.route('/hello')
def hellow_world():
    return 'Hellow World'

@app.route('/feedback')
def feedback():
    return 'Seind email to info@gmail.com for feedback'

@app.route('/contact')
def contact():
    return 'This is the contact person'

# @app.route('/predict',  methods=["POST"])
# def predict():

#     a= Request.form.get('experience')
#     b= Request.form.get('experience')
#     c= Request.form.get('experience')
    
#     print(a)
#     print(b)
#     print(c)
        
#     return 'This is for predicting'

@app.route('/predict' , methods = ['POST'])
def predict():
    exp = request.form.get('experience')
    score = request.form.get('test_score')
    interview_score = request.form.get('interview_score')

    prediction = model.predict([[int(exp) , int(score) , int(interview_score)]])

    output = round(prediction[0] , 2)

    return render_template('base.html' , prediction_text = f"Employee Salary will be $ {output}")

# @app.route('/welcome')
# def welcome():
#     return 'Welcome to Data Science Course'

if __name__ == '__main__':
    app.run(debug=True)
