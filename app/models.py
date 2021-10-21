from app import db

class Estudiante(db.Model):
    carne = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True)
    carrera = db.Column(db.String(120), index=True)


def __repr__(self):
    return '<Estudiante {}>'.format(self.estudiante)

class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.DateTime, index=True)
    carne = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Cita {}>'.format(self.body)