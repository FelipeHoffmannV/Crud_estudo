# Imports flask methods and fake database
from flask import Flask, Blueprint, render_template, request,redirect, url_for, jsonify
from database.initdb import db
from models.user import User

user_route = Blueprint('user_route', __name__, template_folder='templates')





@user_route.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@user_route.route('/add', methods=['POST'])
def add_user():
    newUser = User(nome=request.form['name'], email=request.form['email'])
    db.session.add(newUser)
    db.session.commit()
    return redirect('/')

@user_route.route('/remove/<int:id>', methods=['DELETE'])
def remove_user(id):
    user = User.query.get_or_404(id)
    if not user:
        return jsonify({"message": "Usuário não encontrado"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário removido com sucesso!"})


@user_route.route('/update', methods=['POST'])
def update_user():
    try:
        user_id = request.form.get('id')
        if not user_id:
            return jsonify({'error': 'id ausente'}), 400

        user = User.query.get_or_404(int(user_id))

        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            return jsonify({'error': 'nome ou email ausente'}), 400

        user.nome = name
        user.email = email

        db.session.commit()
        return jsonify({'message': 'Usuário atualizado com sucesso'}), 200

    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({'error': 'erro interno', 'detail': str(e)}), 500