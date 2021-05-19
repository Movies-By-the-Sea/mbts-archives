from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email

class ReviewForm(FlaskForm):
    name = StringField('Movie Name',validators=[DataRequired()])
    genre1 = StringField('Primary',validators=[DataRequired()])
    genre2 = StringField('Secondary',validators=[DataRequired()])
    director = StringField('Director',validators=[DataRequired()])
    netflix = BooleanField('Netflix', default=True)
    prime = BooleanField('Amazon Prime', default=False)

    review = TextAreaField('Write your review here',validators=[DataRequired()])
    acting = StringField('Acting',validators=[DataRequired()])
    story = StringField('Story',validators=[DataRequired()])
    execution = StringField('Execution',validators=[DataRequired()])
    profundity = StringField('Profundity',validators=[DataRequired()])
    overall = StringField('Overall',validators=[DataRequired()])

    link = StringField('Link to the movie')
    image = FileField('Upload poster for the film',validators=[FileAllowed(['jpg','png'])])

    submit = SubmitField('Submit Review')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Email()])
    password = PasswordField('Password',validators=[DataRequired()]) 
    submit = SubmitField('Login to Admin Panel')