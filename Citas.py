from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.db'
db = SQLAlchemy(app)

class Cita(db.Model):
    hora = 0
    fecha = ""

    hora = db.Column(db.Integrer, primary_key =True)
    fecha= db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.carne
