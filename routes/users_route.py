# Imports flask methods and fake database
from flask import Flask, Blueprint, render_template, request,redirect, url_for
from database.fic_data import users

user_route = Blueprint('user_route', __name__, template_folder='templates')

# Show user route
@user_route.route('/')
def show_user():
    return render_template('index.html', users=users)


# Add user route
@user_route.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    new_id = users[-1]['id'] + 1 if users else 1
    user = {'id': new_id,
            'name': name, 
            'email': email,
            }
    users.append(user.copy())
    print(users)
    return redirect(url_for('user_route.show_user'))



# Update user route
@user_route.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    for user in users:
        if user['id'] == id:
            user['name'] = request.form['name']
            user['email'] = request.form['email']
            break
    return redirect(url_for('user_route.show_user'))



# Remove user route
@user_route.route('/remove/<int:id>')
def remove_user(id):
    for user in users:
        if id == user['id']:
            users.remove(user)  
    return redirect(url_for('user_route.show_user'))