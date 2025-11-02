import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from models.user import User
from database.initdb import db
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_add_user(client):
    response = client.post('/add', data={'name': 'João', 'email': 'joao@test.com'}, follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        user = User.query.filter_by(email='joao@test.com').first()
        assert user is not None
        assert user.nome == 'João'

def test_remove_user(client):
    client.post('/add', data={'name': 'Maria', 'email': 'maria@test.com'}, follow_redirects=True)
    with app.app_context():
        user = User.query.filter_by(email='maria@test.com').first()
        assert user is not None
        user_id = user.id
    response = client.delete(f'/remove/{user_id}')
    assert response.status_code == 200
    with app.app_context():
        user = User.query.filter_by(email='maria@test.com').first()
        assert user is None

def test_show_users_empty(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Nenhum usuario encontrado' in response.data


