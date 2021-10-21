from app import app, db
from flask import render_template, flash, request, redirect
from app.forms import LoginForm, EnteringStudentData, EnteringDatesData, EnteringHistoryData
from app.models import Estudiante, Cita

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)

@app.route('/index', methods=['POST', 'GET'])
def index():
    form = EnteringStudentData()
    if form.validate_on_submit():
        estudiante = Estudiante(carne=form.carne.data, nombre=form.nombre.data, carrera=form.carrera.data)
        db.session.add(estudiante)
        db.session.commit()
        flash('¡Estudiante ingresado con éxito!')
        return redirect(("http://127.0.0.1:5000/index"))
    return render_template('index.html', title='Ingreso', form =form)


@app.route('/calendario', methods=['GET', 'POST'])
def calendario():
    form = EnteringDatesData()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('calendario.html', title='Calendario', form=form)

@app.route('/historial', methods=['GET', 'POST'])
def historial():
    form = EnteringHistoryData()
    return render_template('historial.html', title='Historial', form=form)

    