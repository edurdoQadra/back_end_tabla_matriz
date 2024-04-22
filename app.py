from flask import Flask, jsonify, request
from config import app, db
from models import Matriz

# Obtener todos los clientes
@app.route('/clientes', methods=['GET'])
def get_all_clientes():
    clientes = Matriz.query.limit(20).all()
    clientes_list = []
    for cliente in clientes:
        cliente_dict = {
            'ID': cliente.ID,
            'CODIGOS': cliente.CODIGOS,
            'REPORTES': cliente.REPORTES,
            'DEPARTAMENTO': cliente.DEPARTAMENTO,
            'PROVINCIA': cliente.PROVINCIA,
            'DISTRITO': cliente.DISTRITO,
            'DIRECCION': cliente.DIRECCION,
            'REFERENCIA': cliente.REFERENCIA,
            'ADMINISTRADOR': cliente.ADMINISTRADOR,
            'ASOCIADO': cliente.ASOCIADO,
            'DNI': cliente.DNI,
            'NUMERO': cliente.NUMERO,
            'RAZON_SOCIAL': cliente.RAZON_SOCIAL,
            'RUC': cliente.RUC,
            'BASE_EMPRESA': cliente.BASE_EMPRESA,
            'CORREO': cliente.CORREO,
            'TELEFONO': cliente.TELEFONO
        }
        clientes_list.append(cliente_dict)
    return jsonify({'clientes': clientes_list})

# Obtener un cliente por ID
@app.route('/clientes/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    cliente = Matriz.query.get_or_404(cliente_id)
    cliente_dict = {
        'ID': cliente.ID,
        'CODIGOS': cliente.CODIGOS,
        'REPORTES': cliente.REPORTES,
        'DEPARTAMENTO': cliente.DEPARTAMENTO,
        'PROVINCIA': cliente.PROVINCIA,
        'DISTRITO': cliente.DISTRITO,
        'DIRECCION': cliente.DIRECCION,
        'REFERENCIA': cliente.REFERENCIA,
        'ADMINISTRADOR': cliente.ADMINISTRADOR,
        'ASOCIADO': cliente.ASOCIADO,
        'DNI': cliente.DNI,
        'NUMERO': cliente.NUMERO,
        'RAZON_SOCIAL': cliente.RAZON_SOCIAL,
        'RUC': cliente.RUC,
        'BASE_EMPRESA': cliente.BASE_EMPRESA,
        'CORREO': cliente.CORREO,
        'TELEFONO': cliente.TELEFONO
    }
    return jsonify({'cliente': cliente_dict})

# Crear un nuevo cliente
@app.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.json
    new_cliente = Matriz(**data)
    db.session.add(new_cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente creado correctamente'}), 201

# Actualizar un cliente
@app.route('/clientes/<int:cliente_id>', methods=['PUT'])
def update_cliente(cliente_id):
    cliente = Matriz.query.get_or_404(cliente_id)
    data = request.json
    for key, value in data.items():
        setattr(cliente, key, value)
    db.session.commit()
    return jsonify({'message': 'Cliente actualizado correctamente'})

# Eliminar un cliente
@app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    cliente = Matriz.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente eliminado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)
