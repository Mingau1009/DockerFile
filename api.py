from flask import Flask, jsonify, request

app = Flask(__name__)

# BD fictício
usuarios = {
    "1": {"nome": "João da Silva",
           "email": "joao@exemplo.com",
           "senha": "senha123"},
    "2": {"nome": "Maria do Bairro",
           "email": "maria@exemplo.com",
           "senha": "senha456"},
    "3": {"nome": "Goku Super Saiyajin 3",
           "email": "goku@exemplo.com",
           "senha": "senha789"}
}

@app.route('/usuario/<id_usuario>', methods=['GET'])
def get_user(id_usuario):
    usuario = usuarios.get(id_usuario)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/usuario', methods=['POST'])
def create_user():
    novo_usuario = request.json
    id_usuario = str(len(usuarios)+1)
    usuarios[id_usuario] = novo_usuario
    
    return jsonify({"id_usuario": id_usuario}), 201

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000)