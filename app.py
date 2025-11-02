# This file only run the project and register the blueprint 
# Import the methods to run project
from database.initdb import init_db, db
from flask import Flask, render_template
from routes.users_route import user_route
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'database', 'db.sqlite3')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)


app.register_blueprint(user_route)



if __name__ == '__main__':
    app.run(debug=True)