from flask import Flask, render_template, url_for, request
from flask_mail import Message, Mail
from modules.movies import data, userInput
from modules import app, mail
from modules import forms

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():

    movie_inp = forms.MovieSearch()
    contact_us_home = forms.ContactUs()

    if movie_inp.validate_on_submit():
        get_details = userInput(movie_inp.movie_name.data)
        return render_template('index.html',data=data,result=get_details,movie_input=movie_inp, contact_us=contact_us_home)
    
    if contact_us_home.validate_on_submit():
        msg = Message(contact_us_home.subject.data, sender='saumya.bhatt106@gmail.com', recipients=['saumya.bhatt106@gmail.com'])
        msg.body = """
        From: %s 
        Email Address: <%s>
        Subject: %s

        Message: 
        %s
        """ % (contact_us_home.name.data, contact_us_home.email.data,contact_us_home.subject.data, contact_us_home.message.data)
        mail.send(msg)
        return render_template('success_msg.html')

    total_revs = len(data)
    latest_revs = data[-3:]
    temp_result = userInput('Get Out')
    return render_template('index.html',total_revs=total_revs, latest_revs=latest_revs, data=data, movie_input=movie_inp,result=temp_result, contact_us=contact_us_home)

@app.route('/reviews', methods=['GET','POST'])
def review():
    contact_us_review = forms.ContactUs()
    if contact_us_review.validate_on_submit():
        msg = Message(contact_us_review.subject.data, sender='saumi10600@gmail.com', recipients=['saumya.bhatt106@gmail.com'])
        msg.body = """
        From: %s 
        Email Address: <%s>
        Subject: %s

        Message: 
        %s
        """ % (contact_us_review.name.data, contact_us_review.email.data,contact_us_review.subject.data, contact_us_review.message.data)
        mail.send(msg)
        return render_template('success_msg.html')
    return render_template('reviews.html', data=data, contact_us=contact_us_review)


@app.route('/<int:movie_id>')
def get_review(movie_id):
    review = data[movie_id-1]
    if review['Overall'] > 3.9:
        percent = int((review['Overall']/4.5)*100)
    else:
        percent = int((review['Overall']/4)*100)
    return render_template('movie_review.html',review=review, percent=percent)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html')
