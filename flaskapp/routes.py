from flask import render_template, url_for, flash, redirect, request
from flask.globals import request
from flaskapp import app, db
from flaskapp.forms import Question, QuestionCreaterForm, AnotherQuestionsForm, qs1, qs2
from flaskapp.models import User, Questions


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/qresults",  methods=["GET", "POST"])
def questions_results():
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

    return render_template('questions_results.html', correct=correct)


@app.route("/menu", methods=["GET", "POST"])
def menu():
    return render_template('menu.html')

@app.route("/qs1", methods=["GET", "POST"])
def question_set_1():
    global formqsr1
    formqsr1 = qs1()
    if formqsr1.validate_on_submit():
        return redirect(url_for('question_set_results_1'))
    return render_template('qs1.html', form=formqsr1)


@app.route("/qs2", methods=["GET", "POST"])
def question_set_2():
    global formqsr2
    formqsr2 = qs2()
    if formqsr2.validate_on_submit():
        return redirect(url_for('question_set_results_2'))
    return render_template('qs2.html', form=formqsr2)

@app.route("/qsr1", methods=["GET", "POST"])
def question_set_results_1():
    form = formqsr1
    wrong = 0
    wrong2 = 0
    wrong3 = 0
    wrong4 = 0
    wrong5 = 0
    quest = Questions.query.all()
    correct = 0
    q1 = request.form['q11']
    q2 = request.form['q12']
    q3 = request.form['q13']
    q4 = request.form['q14']
    q5 = request.form['q15']
    if q1 == quest[0].answer:
        correct += 1
    else:
        if q1 == '2018':
            wrong = 1
        elif q1 == '2020':
            wrong = 2
        elif q1 == '2017':
            wrong = 3
    if q2 == quest[1].answer:
        correct += 1
    else:
        if q2 == '6':
            wrong2 = 1
        elif q2 == '12':
            wrong2 = 2
        elif q2 == '14':
            wrong2 = 3
    if q3 == quest[2].answer:
        correct += 1
    else:
        if q3 == 'Hiroshima':
            wrong3 = 1
        elif q3 == 'Kyoto':
            wrong3 = 2
        elif q3 == 'Beijing':
            wrong3 = 3
    if q4 == quest[3].answer:
        correct += 1
    else:
        if q4 == 'Pound sign':
            wrong4 = 1
        elif q4 == 'Four-line':
            wrong4 = 2
        elif q4 == 'Asterisk':
            wrong4 = 3
    if q5 == quest[4].answer:
        correct += 1
    else:
        if q5 == 'Air pressure':
            wrong5 = 1
        elif q5 == 'Gravity':
            wrong5 = 2
        elif q5 == 'Moisture':
            wrong5 = 3
    return render_template('qsr1.html', correct=correct, wrong=wrong, wrong2=wrong2, wrong3=wrong3, wrong4=wrong4, wrong5=wrong5)


@app.route("/qsr2", methods=["GET", "POST"])
def question_set_results_2():
    form = formqsr2
    correct = 0
    quest = Questions.query.all()
    q1 = request.form['q21']
    q2 = request.form['q22']
    q3 = request.form['q23']
    q4 = request.form['q24']
    q5 = request.form['q25']
    if q1 == quest[5].answer:
        correct += 1
    if q2 == quest[6].answer:
        correct += 1
    if q3 == quest[7].answer:
        correct += 1
    if q4 == quest[8].answer:
        correct += 1
    if q5 == quest[9].answer:
        correct += 1
    return render_template('qsr2.html', correct=correct)





@app.route("/questions", methods=["GET", "POST"])
def questions():
    form = Question()
    if form.validate_on_submit():
        return redirect(url_for('questions_results'))

    return render_template('questions.html', form=form)




@app.route("/results", methods=["GET", "POST"])
def results():
    form = form1
    q1 = request.form['q11']
    q2 = request.form['q22']
    return render_template('results.html')


@app.route("/newquestions", methods=['GET', 'POST'])
def new_questions():
    form = QuestionCreaterForm()
    if form.validate_on_submit():
        question = Questions(question=form.question.data, choice1=form.choice1.data, choice2=form.choice2.data,
                             choice3=form.choice3.data, choice4=form.choice4.data, answer=form.answer.data)
        db.session.add(question)
        db.session.commit()
        flash('You entered the data successfully into the database!', 'success')
        return redirect(url_for('new_questions'))

    return render_template('new_questions.html', title="New Questions", form=form)

@app.route("/testing", methods=['GET', 'POST'])
def testing():
    # global correct
    # correct = 0
    global form1
    ques = Questions.query.all()
    form1 = AnotherQuestionsForm()
    if form1.validate_on_submit():
        q1 = form1.q1.data
        q2 = form1.q2.data
        ques = Questions.query.all()
        # if q1 == ques.answer:
        #
        # if q2 == ques[1]:
        #     correct += 1

        return redirect(url_for('results'))
    return render_template('testing.html', form=form1)
