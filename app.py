from flask import Flask, request, render_template, redirect, flash
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, satisfaction_survey

app = Flask(__name__)
debug = DebugToolbarExtension(app)

responses = list()

@app.route('/')
def home_route():
    return render_template('base.html', survey=satisfaction_survey)

@app.route('/survey')
def take_survey():
    return render_template('survey', survey=satisfaction_survey)