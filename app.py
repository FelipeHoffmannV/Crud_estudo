# This file only run the project and register the blueprint 
# Import the methods to run project
from database.fic_data import users
from flask import Flask
from routes.users_route import user_route

app = Flask(__name__)



app.register_blueprint(user_route)



if __name__ == '__main__':
    app.run(debug=True)