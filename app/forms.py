from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.fields.html5 import DateField, TimeField
from wtforms import validators
from wtforms.fields.core import IntegerField, StringField
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

class EnteringDatesData(FlaskForm):
    fecha = DateField('Fecha',validators=[DataRequired()], format='%d/%m/%Y')
    hora = TimeField('Hora', validators=[DataRequired()], format='%H:%M', default=datetime.now())
    carne = IntegerField('Carne', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class EnteringHistoryData(FlaskForm):
    carne = IntegerField('Numero de Carne', validators=[DataRequired()])
    submit = SubmitField('Buscar')