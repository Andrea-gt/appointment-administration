from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, validators
from wtforms.fields.html5 import DateField, TimeField
from wtforms.fields.core import IntegerField, StringField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordar Contraseña')
    submit = SubmitField('Ingresar')

class RegistrationForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField(
        'Repita la contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor ingrese un usuario distinto')

class EnteringStudentData(FlaskForm):
    nombre = StringField('Nombre de Estudiante', validators=[DataRequired()])
    carne = IntegerField('Numero de Carne', validators=[DataRequired()])
    carrera = StringField('Carrera de Estudiante', validators=[DataRequired()])
    submit = SubmitField('Ingresar Datos')

class EnteringDatesData(FlaskForm):
    fecha = DateField('Fecha',validators=[DataRequired()], format='%Y-%m-%d')
    hora = TimeField('Hora', validators=[DataRequired()], format='%H:%M', default=datetime.now())
    carne = IntegerField('Carne', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class EnteringHistoryData(FlaskForm):
    carne = IntegerField('Numero de Carne', validators=[DataRequired()])
    submit = SubmitField('Buscar')