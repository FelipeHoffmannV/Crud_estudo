from flask import Flask, Blueprint, render_template, request,redirect
from database.fic_data import users

user_route = Blueprint('add_user_route', __name__, template_folder='templates')

id_user = 0
@user_route.route('/add', methods=['POST'])
def add_user():
    global id_user
    id_user += 1
    name = request.form['name']
    email = request.form['email']

    user = {'id': id_user,
            'name': name, 
            'email': email,
            }
    users.append(user.copy())
    print(users)
    return render_template('index.html', users=users)


    