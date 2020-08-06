from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Length

# formulario de registro de usuarios

class SignupForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(),Length(min=3, max=50, message="Nombre incorrecto")])
    apellidos = StringField('Apellidos', validators=[DataRequired(),Length(min=10, max=80, message=" Apellido incorrecto")])
    sexo = SelectField('Genero', choices = [('H','Hombre'), ('M','Mujer')])
    email = StringField('Email', validators=[DataRequired(),Length(min=6, max=25, message=" Email incorrecto")])
    username = StringField('Username', validators=[DataRequired(),Length(max=10, message=" Username incorrecto")])
    password = PasswordField('Contraseña', validators=[DataRequired(),Length(min=8, max=30, message=" Contraseña invalida")])
    password2 = PasswordField('Repetir contraseña', validators=[DataRequired(),Length(min=8, max=30, message=" Verifique su contraseñas")])

# formulario de inicio de sesion

class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])    
    password = PasswordField('Password', validators=[DataRequired()])

# formulario registro de alumnos

class AlumForm(FlaskForm):
    matricula = StringField('Matricula', validators=[DataRequired(),Length(min=3, max=50, message="Dato incorrecto")])
    nombre = StringField('nombre', validators=[DataRequired(),Length(min=5, max=20, message=" Nombre incorrecto")])
    apellidos = StringField('apellidos', validators=[DataRequired(),Length(min=5, max=20, message=" Apellido incorrecto")])
    genero = SelectField('Genero', choices = [('H','Hombre'), ('M','Mujer')])
    carrera = SelectField('Carrera', choices = [('ISC','Sistemas'), ('IAS','Agronomia'),('LC','Contaduria')])
    generacion = SelectField('Generacion', choices = [('2008-2012','2008-2012'), ('2012-2016','2012-2016'),('2016-2020','2016-2020')])
    estatus = SelectField('Status', choices = [('Titulado','Titulado'), ('No titulado','No titulado')])
    domicilio = StringField('Domicilio', validators=[DataRequired(),Length(min=10, max=100, message="Dato incorrecto")])
    tel = StringField('Telefono', validators=[DataRequired(),Length(min=10, message=" Dato incorrecto")])
    correo = StringField('Correo', validators=[DataRequired(),Length(min=5, max=20, message=" Dato incorrecto")])

# class EstadoForm(FlaskForm):
#     estado = TextAreaField('Publicar algo', validators=[DataRequired(),Length(min=10, max=120, message=" Dato incorrecto")])