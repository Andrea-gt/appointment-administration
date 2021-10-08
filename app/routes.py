from app import app
from flask import render_template, flash, request, redirect, url_for
from app.forms import LoginForm, EnteringStudentData, EnteringDatesData, EnteringHistoryData

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = EnteringStudentData()
    return render_template('index.html', title='Inicio', form =form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/calendario', methods=['POST', 'GET'])
def calendario():
    form = EnteringDatesData()
    return render_template('calendario.html', title='Calendario', form =form)

@app.route('/')
@app.route('/historial', methods=['POST', 'GET'])
def historial():
    form = EnteringHistoryData()
    return render_template('historial.html', title='Historial', form =form)

    