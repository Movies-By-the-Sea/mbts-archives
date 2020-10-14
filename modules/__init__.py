from flask import Flask
from flask_mail import Mail

app = Flask('__name__')
app.config['SECRET_KEY'] = '6D597133743677397A24432646294A404E635266556A586E5A72347537782141'
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'saumya.bhatt106@gmail.com'
app.config["MAIL_PASSWORD"] = 'tsiralzgmliklfzu'
mail = Mail()
mail.init_app(app)

from modules import routes