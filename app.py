import datetime
import uuid
import os

from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_session import Session
from pymongo import MongoClient
from redis import Redis
from forms import *


app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

# conexion a la base de datos
mongo = MongoClient("mongodb://bdd_mongo:27017/")
# crear base de datos
mongodb = mongo.testdb

redis = Redis(host="bdd_redis")

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis

Session(app)


# ruta home
@app.route("/")
def timeline():

    user = session.get('profile')
    if not user:
        return redirect(url_for('login'))   
    return render_template("home.html", user=user)
    
   
# ruta para el registro de usuarios
@app.route("/signup", methods=["GET", "POST"])
def signup():
    form= SignupForm()
    if form.validate_on_submit():
        user = {
            'nombre': form.nombre.data,
            'apellidos': form.apellidos.data,
            'sexo': form.sexo.data,
            'email': form.email.data,
            'username': form.username.data,
            'password': form.password.data
        }
        
        mongodb.users.insert_one(user)        
        return redirect(url_for("login"))        
        
    return render_template("signup.html", form=form)

# ruta login
@app.route("/login",methods=["GET", "POST"])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        user = mongodb.users.find_one({
            'username':form.username.data,
            'password':form.password.data

        })

        if not user:            
            flash('Invalid User/Password')
            return redirect(url_for('login'))
        session['profile'] = user
        return redirect(url_for('timeline'))       
        
    return render_template("login.html", form=form)

# ruta logout
@app.route("/logout")
def logout():
    session['profile'] = None
    return redirect(url_for('timeline'))


# ruta para el registro de alumnos
@app.route("/alumnos", methods=["GET", "POST"])
def addAlumnos():

    user = session.get('profile')
    if not user:
        return redirect(url_for('login'))

    form = AlumForm()

    if form.validate_on_submit():
        alumnos = {

            'matricula': form.matricula.data,
            'nombre': form.nombre.data,
            'apellidos': form.apellidos.data,
            'genero': form.genero.data,
            'carrera': form.carrera.data,
            'generacion': form.generacion.data,
            'status': form.estatus.data,
            'domicilio': form.domicilio.data,
            'telefono': form.tel.data,
            'correo': form.correo.data,
        }
        
        mongodb.alumnos.insert_one(alumnos)        
        return redirect(url_for("addAlumnos"))
           
    return render_template("alumnos.html", form=form, user=user)
    # consulta
    


# ruta de consulta de alumnos
@app.route("/alumnos/consulta")
def consulta_Alum():
    
    user = session.get('profile')
    if not user:
        return redirect(url_for('login'))

    query = list(mongodb.alumnos.find())
    for q in query:        
        q = mongodb.alumnos.find_one()       
       
        
    return render_template("consulta_Alumnos.html", user=user, query=query)
    

# ruta para eliminar alumnos
@app.route('/consulta/delete')
@app.route('/consulta/delete/<matricula>/', methods=['GET'])
def delete_Alumno(matricula):
    delete = mongodb.alumnos
    user = delete.find_one({'matricula':matricula})
    delete.remove(user)
    return redirect(url_for('consulta_Alum'))



@app.route('/admin')
def admin():

    user = session.get('profile')
    if not user:
        return redirect(url_for('login'))

    users = list(mongodb.users.find())
    for u in users:        
        u = mongodb.users.find_one()     
       
        
    return render_template("admin.html", user=user, users=users)
    

  
    return redirect(url_for("admin"))


   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
