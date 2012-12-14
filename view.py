from flask import session, render_template, jsonify, request
from markupsafe import escape

from models import Skill, Project, Client, Category, Info
from config import STATIC_URL, DEBUG, EMAIL as TO, GOOGLE_ANALYTICS, IMAGES_URL


def index():
    """ Index page
    """
    prop = dict()

    prop['skills'] = Skill.query.all()
    prop['projects'] = Project.query.all()
    prop['clients'] = Client.query.all()
    prop['categories'] = Category.query.all()

    prop['STATIC_URL'] = STATIC_URL
    prop['DEBUG'] = DEBUG
    prop['IMAGES_URL']= IMAGES_URL

    prop['title'] = Info.get_param('title')
    prop['about'] = Info.get_param('about')
    prop['google_analytics'] = GOOGLE_ANALYTICS

    if 'username' in session:
        prop['username'] = escape(session['username'])

    return render_template('index.html', **prop)


def sendmail():

    return_array = {}
    return_array['success'] = '1'
    return_array['name_msg'] = request.form['name']
    return_array['email_msg'] = request.form['email']
    return_array['message_msg'] = request.form['message']
    return_array['subject'] = request.form['subject']


    import smtplib
    import string

    MESSAGE = "Email = {0}\r\nName = {1}\r\nMessage={2}".format(return_array['email_msg'], return_array['name_msg'],
        return_array['message_msg'])

    BODY = string.join((
        "From: %s" % return_array['email_msg'],
        "To: %s" % TO,
        "Subject: %s" % return_array['subject'],
        "",
        MESSAGE
        ), "\r\n")

    try:
        server = smtplib.SMTP()
        server.connect()
        server.sendmail(return_array['email_msg'], [TO], BODY)
        server.quit()

    except smtplib.SMTPException:
        return jsonify(succes=0)

    return jsonify(**return_array)

