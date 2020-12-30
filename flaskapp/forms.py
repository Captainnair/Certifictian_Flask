from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired

class FieldsRequiredForm(FlaskForm):
    """Require all fields to have content. This works around the bug that WTForms radio
    fields don't honor the `DataRequired` or `InputRequired` validators.
    """

    class Meta:
        def render_field(self, field, render_kw):
            render_kw.setdefault('required', True)
            return super().render_field(field, render_kw)



class QuestionForms(FieldsRequiredForm):
    q1 = RadioField('What is the keyword used in Python the print something.', choices=[("print", "print"),
            ("return", "return"), ("ouput", "output"), ("show", "show")], validators=[DataRequired()])

    q2 = RadioField('What is the keyword used in Python the returns something.',  choices=[("print", "print"),
            ("return", "return"), ("ouput", "output"), ("show", "show")], validators=[InputRequired()])

    q3 = RadioField('What is the name of the if else keyword in python.', choices=[("if_else", "if_else"),
            ("ifelse", "ifelse"), ("elif", "elif"), ("ielse", "ielse")], validators=[DataRequired()])

    q4 = RadioField('What is the keyword that you must write to open a file.', choices=[("open", "open"),
            ('export', 'export'), ("start", "start"), ('close', 'close')], validators=[DataRequired()])
    text = StringField("Test", validators=[])
    submit = SubmitField('Check you Answers')

