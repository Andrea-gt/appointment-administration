from datetime import date
from app import app, db
from flask import render_template, flash, request, redirect
from app.forms import LoginForm, EnteringStudentData, EnteringDatesData, EnteringHistoryData, RegistrationForm
from app.models import Estudiante, Cita, User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect("http://127.0.0.1:5000/index")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuario o contraseña incorrectos')
            return redirect("http://127.0.0.1:5000/login")
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = ("http://127.0.0.1:5000/index")
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = EnteringStudentData()
    if form.validate_on_submit():
        estudiante = Estudiante.query.filter_by(carne = form.carne.data).first()
        if estudiante is None:
            estudiante = Estudiante(nombre=form.nombre.data, carne = form.carne.data, carrera = form.carrera.data)
            db.session.add(estudiante)
            db.session.commit()
            flash('¡Estudiante ingresado con exito!')
            return redirect("/index")
        flash("Este estudiante ya esta registrado")
    estudiantes = Estudiante.query.order_by(Estudiante.nombre)
    return render_template('index.html', title='Ingreso', form =form, estudiantes = estudiantes)

@app.route('/appointments', methods=['GET', 'POST'])
@login_required
def calendario():
    form = EnteringDatesData()
    if form.validate_on_submit():
        cita = Cita(fecha = form.fecha.data, carne = form.carne.data, hora = form.hora.data)
        db.session.add(cita)
        db.session.commit()
        flash('¡Cita agendada con exito!')
        return redirect("/appointments")

    citas = Cita.query.order_by(Cita.fecha)
    return render_template('appointments.html', title='Citas', form =form, citas = citas)

@app.route('/historial', methods=['GET', 'POST'])
@login_required
def historial():
    form = EnteringHistoryData()
    carneC = form.carne.data
    if form.validate_on_submit():
        cita = Cita.query.filter_by(carne = form.carne.data)
        if cita == carneC:
            flash('Datos filtrados exitosamente')
            return redirect("/historial")
    citas = Cita.query.filter_by(carne = carneC)
    return render_template('historial.html', title='Historial', form=form, citas = citas)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(("http://127.0.0.1:5000/index"))   

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect("http://127.0.0.1:5000/login")
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('¡Ha sido registrado con exito!')
        return redirect("http://127.0.0.1:5000/login")
    return render_template('register.html', title='Register', form=form)