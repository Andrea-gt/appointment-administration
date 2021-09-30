from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    carne = 0
    nombre = ""

    carne = db.Column(db.Integrer, primary_key =True)
    nombre = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.carne