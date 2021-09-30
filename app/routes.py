from usuario import usuario
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():

    psicologo = usuario("Andrea")
    user = {'username': psicologo.nombreUsuario}
    return render_template('index.html', title='Inicio', user=user)