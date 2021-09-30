from usuario import usuario
from app import app
from flask import render_template, request


@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():

    psicologo = usuario("Andrea")
    user = {'username': psicologo.nombreUsuario}

    if request.method == "POST":
        name_content = request.form["content"]

    else:
        return render_template('index.html', title='Inicio', user=user)

    