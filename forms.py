from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  TextAreaField
from wtforms.validators import DataRequired, Length


class SignupForm(FlaskForm):
    name = StringField('User name', validators=[DataRequired(),Length(min=3, max=50, message="Nombre incorrecto")])
    apellidos = StringField('Apellidos', validators=[DataRequired(),Length(min=10, max=80, message=" Apellido incorrecto")])
    biografia = TextAreaField('Biografia', validators=[DataRequired(),Length(min=10, max=120, message=" Biografia incorrecto")])
    email = StringField('Email', validators=[DataRequired(),Length(min=6, max=25, message=" Email incorrecto")])
    telefono = StringField('Telefono', validators=[DataRequired(),Length(max=10, message=" Numero incorrecto")])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8, max=30, message=" Contraseña invalida")])

class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired()])    
    password = PasswordField('Password', validators=[DataRequired()])

class EstadoForm(FlaskForm):
    estado = TextAreaField('Publicar algo', validators=[DataRequired(),Length(min=10, max=120, message=" Dato incorrecto")])