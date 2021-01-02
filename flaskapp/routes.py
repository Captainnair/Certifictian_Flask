from flask import render_template, url_for, flash, redirect, request
from flask.globals import request
from flaskapp import app
from flaskapp.forms import QuestionForms, QuestionCreaterForm
from flaskapp.models import User, Questions


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/questions", methods=["GET", "POST"])
def questions():
    form = QuestionForms()
    if form.validate_on_submit():
        return redirect(url_for('results'))

    return render_template('questions.html', form=form)




@app.route("/results", methods=["GET", "POST"])
def results():

    correct = 0
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    if q1 == 'print':
        correct += 1
    if q2 == 'return':
        correct += 1
    if q3 == 'elif':
        correct += 1
    if q4 == 'open':
        correct += 1

    return render_template('results.html', correct=correct)


@app.route("/newquestions", methods=['GET', 'POST'])
def new_questions():
    form = QuestionCreaterForm()
    if form.validate_on_submit():
        flash('You entered the data successfully into the database!', 'success')
        return redirect(url_for('new_questions'))

    return render_template('new_questions.html', title="New Questions", form=form)
