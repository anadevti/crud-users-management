from flask import Blueprint, render_template, request
from database.client import CLIENTS

client_route = Blueprint('client', __name__)

"""
Rotas de clientes:

    - /clientes/ (GET) - Lista todos os clientes
    - /clientes/ (POST) - inserir um novo cliente no server
    - /clientes/new (GET) - Retorna o formulário para inserir um novo cliente
    - /clientes/<id> (GET) - obter dados de um cliente
    - /clientes/<id>/edit (GET) - Retorna o formulário para editar um cliente
    - /clientes/<id>/update (PUT) - Atualiza os dados de um cliente 
    - /clientes/<id>/delete (DELETE) - Deleta o registro do cliente
"""

@client_route.route('/', methods=['GET'])
def list_clients():
    return render_template('list_clients.html', clients=CLIENTS)

@client_route.route('/', methods=['POST'])
def insert_clients():
    # Lógica para inserir um novo cliente
    return render_template('index.html')

@client_route.route('/new', methods=['GET'])
def form_clients():
    return render_template('form_clients.html')

@client_route.route('/<int:client_id>', methods=['GET'])
def details_clients(client_id):
    return render_template('details_clients.html')

@client_route.route('/<int:client_id>/edit', methods=['GET'])
def form_edit_clients(client_id):
    return render_template('form_edit_clients.html')

@client_route.route('/<int:client_id>/update', methods=['PUT'])
def update_clients(client_id):
    # Lógica para atualizar os dados do cliente
    pass

@client_route.route('/<int:client_id>/delete', methods=['DELETE'])
def delete_clients(client_id):
    # Lógica para deletar o cliente
    pass
