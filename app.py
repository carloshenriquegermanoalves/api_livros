#APIs - São lugares para disponibilizar recursos e/ou funcionalidades
#Passos da API:
# 1. Objetivo - Criar um API para disponibilizar a consulta, criação, edição e exclusão de livros
# 2. URL base - Lugar para onde serão feitas as requisições
    # Usaremos o localhost
# 3. Endpoints - Os tipos de funcionalidades que serão disponibilizados
    # - localhost/livros (GET) - acessaremos todos os livros
    # - localhost/livros/id (GET) - acessaremos um livro específico por seu ID
    # - localhost/livros/id (PUT) - modificaremos as informações de um livro por seu ID
    # - localhost/livros/id (DELETE) - deletaremos um livro por seu ID
# 4. Recursos - Os recursos devolvidos são os livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K.Rowling'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Câmara Secreta',
        'autor': 'J.K.Rowling'
    },
    {
        'id': 3,
        'título': 'Harry Potter e o Prisioneiro de Azkaban',
        'autor': 'J.K.Rowling'
    },
    {
        'id': 4,
        'título': 'Harry Potter e o Cálice de Fogo',
        'autor': 'J.K.Rowling'
    },
    {
        'id': 5,
        'título': 'Harry Potter e a Ordem da Fenix',
        'autor': 'J.K.Rowling'
    },
    {
        'id': 6,
        'título': 'Harry Potter e o Enigma do Príncipe',
        'autor': 'J.K.Rowling'
    },
    {
        'id': 7,
        'título': 'Harry Potter e as Relíquias da Morte',
        'autor': 'J.K.Rowling'
    }
]

# Para consultar todos os livros:
@app.route('/livros',methods=['GET'])
def mostrar_livros():
    return jsonify(livros)

# Para consultar um livro por id:
@app.route('/livros/<int:id>', methods=['GET'])
def consultar_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Para editar livros por id, pois só poderá ser editado um livro por vez:
@app.route('/livros/<int:id>',methods=['PUT'])
def modificar_livro_por_id(id):
    livro_modificado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_modificado)
            return jsonify(livros[indice])

# Para criar um novo livro:
@app.route('/livros', methods=['POST'])
def adicionar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Para excluir um livro:
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)
