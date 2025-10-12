# Tests 
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app, users


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        users.clear()
        yield client


def test_add_user(client):
    print('\n🧩 [1/4] Adding user...')
    time.sleep(1)
    response = client.post('/add', data={'name': 'João', 'email': 'joao@test.com'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Jo\xc3\xa3o' in response.data 
    assert len(users) == 1
    assert users[0]['name'] == 'João'
    print('✅ User João success')
    time.sleep(1.5)


def test_remove_user(client):
    print('\n🗑️ [2/4] Removing user...')
    time.sleep(1)
    client.post('/add', data={'name': 'Maria', 'email': 'maria@test.com'}, follow_redirects=True)
    user_id = users[0]['id']
    time.sleep(1)
    response = client.get(f'/remove/{user_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Maria' not in response.data
    assert len(users) == 0
    print('✅ User Maria success remove!')
    time.sleep(1.5)


def test_show_users_empty(client):
    print('\n📋 [3/4] Verify empty list...')
    time.sleep(1)
    response = client.get('/')
    assert response.status_code == 200
    assert b'Nenhum usu\xc3\xa1rio cadastrado' in response.data
    print('✅ Empty list pass!')
    time.sleep(1.5)


def test_update_user(client):
    print('\n✏️ [4/4] Update user...')
    time.sleep(1)
    client.post('/add', data={'name': 'Carlos', 'email': 'carlos@test.com'}, follow_redirects=True)
    user_id = users[0]['id']
    time.sleep(1)
    print(f'🔧 Update user data for id: {user_id}...')
    response = client.post(f'/update/{user_id}', data={'name': 'Carlos Silva', 'email': 'carlos.silva@test.com'}, follow_redirects=True)
    time.sleep(1)

    assert response.status_code == 200  
    assert b'Carlos Silva' in response.data  
    assert b'carlos.silva@test.com' in response.data  
    assert users[0]['name'] == 'Carlos Silva'
    assert users[0]['email'] == 'carlos.silva@test.com'

    print('✅ User update success!')
    time.sleep(1.5)
