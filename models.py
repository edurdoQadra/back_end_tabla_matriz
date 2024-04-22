from config import db

class Matriz(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    CODIGOS = db.Column(db.Integer)
    REPORTES = db.Column(db.String(255))
    DEPARTAMENTO = db.Column(db.String(255))
    PROVINCIA = db.Column(db.String(255))
    DISTRITO = db.Column(db.String(255))
    DIRECCION = db.Column(db.String(255))
    REFERENCIA = db.Column(db.String(255))
    ADMINISTRADOR = db.Column(db.String(255))
    ASOCIADO = db.Column(db.String(255))
    DNI = db.Column(db.String(20))
    NUMERO = db.Column(db.String(20))
    RAZON_SOCIAL = db.Column(db.String(255))
    RUC = db.Column(db.String(20))
    BASE_EMPRESA = db.Column(db.String(255))
    CORREO = db.Column(db.String(255))
    TELEFONO = db.Column(db.String(20))


# class Clientes(db.Model):
#     Id = db.Column(db.Integer, primary_key=True)
#     Converted = db.Column(db.String(200), nullable=False)
#     Status = db.Column(db.String(200), nullable=False)
#     Creation = db.Column(db.String(200), nullable=False)
#     Update = db.Column(db.String(200), nullable=False)
#     Username = db.Column(db.String(200), nullable=False)
#     Name = db.Column(db.String(200), nullable=False)
#     Surname = db.Column(db.String(200), nullable=False)
#     Mobile = db.Column(db.String(200), nullable=False)
#     Correo = db.Column(db.String(200), nullable=False)

