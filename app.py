
from flask import Flask,render_template
from routes.users_route import user_route
from database.fic_data import users

app = Flask(__name__)



app.register_blueprint(user_route)


print(users)


if __name__ == '__main__':
    app.run(debug=True)