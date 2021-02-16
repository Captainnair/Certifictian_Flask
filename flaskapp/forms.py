from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from flaskapp.models import Questions
from flaskapp import db
import random

class FieldsRequiredForm(FlaskForm):
    """Require all fields to have content. This works around the bug that WTForms radio
    fields don't honor the `DataRequired` or `InputRequired` validators.
    """

    class Meta:
        def render_field(self, field, render_kw):
            render_kw.setdefault('required', True)
            return super().render_field(field, render_kw)



class AnotherQuestionsForm(FieldsRequiredForm):
    hello = Questions.query.all()
    id = 1
    question1 = Questions.query.filter_by(id=id).first()
    question2 = Questions.query.filter_by(id=(id + 1)).first()
    q11 = RadioField(str(question1.question), choices=[(str(question1.choice1), str(question1.choice1)), (str(question1.choice2), str(question1.choice2)),
                                                               (str(question1.choice3), str(question1.choice3)), (str(question1.choice4), str(question1.choice4))])
    q22 = RadioField(str(question2.question), choices=[(str(question2.choice1), str(question2.choice1)), (str(question2.choice2), str(question2.choice2)),
                                                               (str(question2.choice3), str(question2.choice3)), (str(question2.choice4), str(question2.choice4))])
    submit = SubmitField('Check you Answers')



class Question(FieldsRequiredForm):



    q1 = RadioField('What is the keyword used in Python the print something.', choices=[("print", "print"),
                                                                                        ("return", "return"),
                                                                                        ("ouput", "output"),
                                                                                        ("show", "show")],
                    validators=[DataRequired()])

    q2 = RadioField('What is the keyword used in Python the returns something.', choices=[("print", "print"),
                                                                                          ("return", "return"),
                                                                                          ("ouput", "output"),
                                                                                          ("show", "show")],
                    validators=[InputRequired()])

    q3 = RadioField('What is the name of the if else keyword in python.', choices=[("if_else", "if_else"),
                                                                                   ("ifelse", "ifelse"),
                                                                                   ("elif", "elif"),
                                                                                   ("ielse", "ielse")],
                    validators=[DataRequired()])

    q4 = RadioField('What is the keyword that you must write to open a file.', choices=[("open", "open"),
                                                                                        ('export', 'export'),
                                                                                        ("start", "start"),
                                                                                        ('close', 'close')],
                    validators=[DataRequired()])

    # q1 = RadioField('What is the keyword used in Python the print something.', choices=[("print", "print"),
    #         ("return", "return"), ("ouput", "output"), ("show", "show")], validators=[DataRequired()])
    #
    # q2 = RadioField('What is the keyword used in Python the returns something.',  choices=[("print", "print"),
    #         ("return", "return"), ("ouput", "output"), ("show", "show")], validators=[InputRequired()])
    #
    # q3 = RadioField('What is the name of the if else keyword in python.', choices=[("if_else", "if_else"),
    #         ("ifelse", "ifelse"), ("elif", "elif"), ("ielse", "ielse")], validators=[DataRequired()])
    #
    # q4 = RadioField('What is the keyword that you must write to open a file.', choices=[("open", "open"),
    #         ('export', 'export'), ("start", "start"), ('close', 'close')], validators=[DataRequired()])
    text = StringField("Test", validators=[])
    submit = SubmitField('Check you Answers')

class qs1(FieldsRequiredForm):
    global quest
    question_list1 = []
    i = 1
    quest = Questions.query.all()
    for question in quest:
        if i == 5:
            quest.append(question)
            quest.remove(question)
            i += 1
    q11 = RadioField(str(quest[0].question), choices=[(str(quest[0].choice1), str(quest[0].choice1)),
                                                       (str(quest[0].choice2), str(quest[0].choice2)),
                                                       (str(quest[0].choice3), str(quest[0].choice3)),
                                                       (str(quest[0].choice4), str(quest[0].choice4))])

    q12 = RadioField(str(quest[1].question), choices=[(str(quest[1].choice1), str(quest[1].choice1)),
                                                      (str(quest[1].choice2), str(quest[1].choice2)),
                                                      (str(quest[1].choice3), str(quest[1].choice3)),
                                                      (str(quest[1].choice4), str(quest[1].choice4))])

    q13 = RadioField(str(quest[2].question), choices=[(str(quest[2].choice1), str(quest[2].choice1)),
                                                      (str(quest[2].choice2), str(quest[2].choice2)),
                                                      (str(quest[2].choice3), str(quest[2].choice3)),
                                                      (str(quest[2].choice4), str(quest[2].choice4))])

    q14 = RadioField(str(quest[3].question), choices=[(str(quest[3].choice1), str(quest[3].choice1)),
                                                      (str(quest[3].choice2), str(quest[3].choice2)),
                                                      (str(quest[3].choice3), str(quest[3].choice3)),
                                                      (str(quest[3].choice4), str(quest[3].choice4))])

    q15 = RadioField(str(quest[4].question), choices=[(str(quest[4].choice1), str(quest[4].choice1)),
                                                      (str(quest[4].choice2), str(quest[4].choice2)),
                                                      (str(quest[4].choice3), str(quest[4].choice3)),
                                                      (str(quest[4].choice4), str(quest[4].choice4))])
    submit = SubmitField('Check you Answers')


class qs2(FieldsRequiredForm):
    global quest
    question_list2 = []
    i = 1
    que = Questions.query.all()
    for question in que:
        if question.id > 5:
            question_list2.append(question)

    q21 = RadioField(str(question_list2[0].question), choices=[(str(question_list2[0].choice1), str(question_list2[0].choice1)),
                                                       (str(question_list2[0].choice2), str(question_list2[0].choice2)),
                                                       (str(question_list2[0].choice3), str(question_list2[0].choice3)),
                                                       (str(question_list2[0].choice4), str(question_list2[0].choice4))])

    q22 = RadioField(str(question_list2[1].question), choices=[(str(question_list2[1].choice1), str(question_list2[1].choice1)),
                                                      (str(question_list2[1].choice2), str(question_list2[1].choice2)),
                                                      (str(question_list2[1].choice3), str(question_list2[1].choice3)),
                                                      (str(question_list2[1].choice4), str(question_list2[1].choice4))])

    q23 = RadioField(str(question_list2[2].question), choices=[(str(question_list2[2].choice1), str(question_list2[2].choice1)),
                                                      (str(question_list2[2].choice2), str(question_list2[2].choice2)),
                                                      (str(question_list2[2].choice3), str(question_list2[2].choice3)),
                                                      (str(question_list2[2].choice4), str(question_list2[2].choice4))])

    q24 = RadioField(str(question_list2[3].question), choices=[(str(question_list2[3].choice1), str(question_list2[3].choice1)),
                                                      (str(question_list2[3].choice2), str(question_list2[3].choice2)),
                                                      (str(question_list2[3].choice3), str(question_list2[3].choice3)),
                                                      (str(question_list2[3].choice4), str(question_list2[3].choice4))])

    q25 = RadioField(str(question_list2[4].question), choices=[(str(question_list2[4].choice1), str(question_list2[4].choice1)),
                                                      (str(question_list2[4].choice2), str(question_list2[4].choice2)),
                                                      (str(question_list2[4].choice3), str(question_list2[4].choice3)),
                                                      (str(question_list2[4].choice4), str(question_list2[4].choice4))])
    submit = SubmitField('Check you Answers')

class QuestionCreaterForm(FlaskForm):
    question = TextAreaField('Enter the question:', validators=[DataRequired()])
    choice_1 = StringField('Enter the 1st choice:', validators=[DataRequired()])
    choice_2 = StringField('Enter the 2nd choice:', validators=[DataRequired()])
    choice_3 = StringField('Enter the 3rd choice:', validators=[DataRequired()])
    choice_4 = StringField('Enter the 4th choice:', validators=[DataRequired()])
    answer_1 = StringField('Enter the correct answer:', validators=[DataRequired()])
    submit = SubmitField('Enter Into the Database')



