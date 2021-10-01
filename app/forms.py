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

class EnteringDatesData(FlaskForm):
    fecha = IntegerField('Fecha', validators=[DataRequired()])
    hora = IntegerField('Hora', validators=[DataRequired()])
    estudiante = StringField('Estudiante', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class EnteringHistoryData(FlaskForm):
    nameforhistory = StringField('Nombre para el historial', validators=[DataRequired()])
    submit = SubmitField('Guardar')