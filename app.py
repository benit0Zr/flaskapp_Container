import datetime
import uuid
import os

from flask import Flask, render_template, redirect, url_for, session, flash
from flask_session import Session
from pymongo import MongoClient
from redis import Redis
from forms import *


app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

mongo = MongoClient("mongodb://bdd_mongo:27017/")
mongodb = mongo.testdb

redis = Redis(host="bdd_redis")

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis

Session(app)

@app.route("/", methods=["GET", "POST"])
def timeline():

    user = session.get('profile')
    if not user:
        return redirect(url_for('login'))

    form = EstadoForm()
    if form.validate_on_submit():
        post = {
            'estado': form.estado.data,
            'user_id': user['_id']            
        }

        mongodb.posts.insert_one(post)
        return redirect(url_for('timeline'))


    posts = list(mongodb.posts.find())
    for post in posts:        
        post['user']= mongodb.users.find_one({'_id' : post['user_id']})
   
    return render_template("home.html", form=form, user=user, posts=posts)
    #return str(user)
   

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form= SignupForm()
    if form.validate_on_submit():
        user = {
            'name': form.name.data,
            'apellidos': form.apellidos.data,
            'biografia': form.biografia.data,
            'email': form.email.data,
            'telefono': form.telefono.data,
            'password': form.password.data
        }
        mongodb.users.insert_one(user)
        #return str(user)
        #redireccionar url
        return redirect(url_for("login"))
        
        
    return render_template("signup.html", form=form)


@app.route("/login",methods=["GET", "POST"])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        user = mongodb.users.find_one({
            'email':form.email.data,
            'password':form.password.data


        })

        if not user:
            
            flash('Invalid User/Password')
            return redirect(url_for('login'))
        session['profile'] = user
        return redirect(url_for('timeline'))      
        
        
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    session['profile'] = None
    return redirect(url_for('timeline'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
