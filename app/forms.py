from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms import validators
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordar Contraseña')
    submit = SubmitField('Ingresar')

class EnteringStudentData(FlaskForm):
    nombre = StringField('Nombre de Estudiante', validators=[DataRequired()])
    carne = IntegerField('Numero de Carne', validators=[DataRequired()])
    submit = SubmitField('Ingresar Datos')