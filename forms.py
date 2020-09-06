from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MovieSearch(FlaskForm):
    movie_name = StringField('Enter Movie Name',validators=[DataRequired()])