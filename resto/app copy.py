from flask import Flask, jsonify, request
from config import app, db
from models import Clientes

# Obtener todos los clientes
@app.route('/clients', methods=['GET'])
def get_all_clients():
    clients = Clientes.query.all()
    clients_list = []
    for client in clients:
        client_dict = {
            'Id': client.Id,
            'Converted': client.Converted,
            'Status': client.Status,
            'Creation': client.Creation,
            'Update': client.Update,
            'Username': client.Username,
            'Name': client.Name,
            'Surname': client.Surname,
            'Mobile': client.Mobile,
            'Correo': client.Correo
        }
        clients_list.append(client_dict)
    return jsonify({'clients': clients_list})

# Obtener un cliente por ID
@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Clientes.query.get_or_404(client_id)
    client_dict = {
        'Id': client.Id,
        'Converted': client.Converted,
        'Status': client.Status,
        'Creation': client.Creation,
        'Update': client.Update,
        'Username': client.Username,
        'Name': client.Name,
        'Surname': client.Surname,
        'Mobile': client.Mobile,
        'Correo': client.Correo
    }
    return jsonify({'client': client_dict})

# Crear un nuevo cliente
@app.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    new_client = Clientes(**data)
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'Cliente creado correctamente'}), 201

# Actualizar un cliente
@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = Clientes.query.get_or_404(client_id)
    data = request.json
    for key, value in data.items():
        setattr(client, key, value)
    db.session.commit()
    return jsonify({'message': 'Cliente actualizado correctamente'})

# Eliminar un cliente
@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Clientes.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Cliente eliminado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)
