from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  TextAreaField
from wtforms.validators import DataRequired, Length


class SignupForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(),Length(min=3, max=50, message="Nombre incorrecto")])
    apellidos = StringField('Apellidos', validators=[DataRequired(),Length(min=10, max=80, message=" Apellido incorrecto")])
    sexo = StringField('Sexo', validators=[DataRequired(),Length(min=5, max=20, message=" Dato incorrecto")])
    email = StringField('Email', validators=[DataRequired(),Length(min=6, max=25, message=" Email incorrecto")])
    username = StringField('Username', validators=[DataRequired(),Length(max=10, message=" Username incorrecto")])
    password = PasswordField('Contraseña', validators=[DataRequired(),Length(min=8, max=30, message=" Contraseña invalida")])
    password2 = PasswordField('Repetir contraseña', validators=[DataRequired(),Length(min=8, max=30, message=" Verifique su contraseñas")])

class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])    
    password = PasswordField('Password', validators=[DataRequired()])


class AlumForm(FlaskForm):
    matricula = StringField('Matricula', validators=[DataRequired(),Length(min=3, max=50, message="Dato incorrecto")])
    nombre = StringField('nombre', validators=[DataRequired(),Length(min=10, max=80, message=" Nombre incorrecto")])
    apellidos = StringField('apellidos', validators=[DataRequired(),Length(min=5, max=20, message=" Apellido incorrecto")])
    genero = StringField('Genero', validators=[DataRequired(),Length(min=5, max=20, message=" Dato incorrecto")])
    carrera = StringField('Carrera', validators=[DataRequired(),Length(min=6, max=25, message=" Dato incorrecto incorrecto")])
    generacion = StringField('Generacion', validators=[DataRequired(),Length(max=10, message=" Dato incorrecto")])
    estatus = PasswordField('Status', validators=[DataRequired(),Length(min=8, max=30, message="Dato incorrecto")])
    domicilio = PasswordField('Domicilio', validators=[DataRequired(),Length(min=8, max=30, message="Dato incorrecto")])
    tel = StringField('Telefono', validators=[DataRequired(),Length(min=5, max=20, message=" Dato incorrecto")])
    correo = StringField('Correo', validators=[DataRequired(),Length(min=5, max=20, message=" Dato incorrecto")])

# class EstadoForm(FlaskForm):
#     estado = TextAreaField('Publicar algo', validators=[DataRequired(),Length(min=10, max=120, message=" Dato incorrecto")])