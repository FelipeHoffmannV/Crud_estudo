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
def addUser():
    newUser = User(nome=request.form['name'], email=request.form['email'])
    db.session.add(newUser)
    db.session.commit()
    return jsonify({"message": 'OK'})

@user_route.route('/remove/<int:id>', methods=['DELETE'])
def removerUser(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')

