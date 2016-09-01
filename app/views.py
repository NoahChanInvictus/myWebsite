from flask import render_template
from app import app

@app.route('/')
def helloworld():
    user = { 'nickname': 'Noah' } # fake user
    return render_template("index.html",\
                           user = user)

@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",\
    	             title = 'home',\
                           user = user)
