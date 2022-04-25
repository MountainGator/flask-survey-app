from crypt import methods
from flask import Flask, request, render_template, redirect, flash
from random import randint, choice, sample
# from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, satisfaction_survey

app = Flask(__name__)
# debug = DebugToolbarExtension(app)

responses = list()

@app.route('/')
def home_route():
    return render_template('base.html', survey=satisfaction_survey)

@app.route('/survey')
def take_survey():
    count = 0
    return render_template('survey.html', survey=satisfaction_survey, count=count)

@app.route('/survey/thank-you', methods=["POST"])
def thank_you():
    for answer in request.form:
        responses.append(answer)
    print(responses)
    return render_template('thank-you.html')