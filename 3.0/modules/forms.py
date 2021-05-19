from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

class MovieSearch(FlaskForm):
    movie_name = StringField('Enter Movie Name',validators=[DataRequired()])

class ContactUs(FlaskForm):
    name = StringField('Enter your name',validators=[DataRequired()])
    email = EmailField('Enter your email', validators=[DataRequired()])
    subject = StringField('Enter your subject', validators=[DataRequired()])
    message = TextAreaField('Enter your message', validators=[DataRequired()])
    submit = SubmitField('Send Message', validators=[DataRequired()])