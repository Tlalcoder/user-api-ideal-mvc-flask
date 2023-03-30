import pytest
from source import create_app, db
from source import User


@pytest.fixture(scope='module')
def new_user():
    user = User(
        name='Test User',
        email='testuser@example.com',
        password='password'
    )
    return user


@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()

        # Create test user
        user = User(
            name='Test User',
            email='testuser@example.com',
            password='password'
        )
        db.session.add(user)
        db.session.commit()

        yield testing_client

        db.session.remove()
        db.drop_all()


def test_register(test_client, new_user):
    # Test user registration
    response = test_client.post(
        '/register',
        json={
            'name': 'Test User',
            'email': 'testuser2@example.com',
            'password': 'password'
        }
    )
    assert response.status_code == 201


def test_register_existing_email(test_client, new_user):
    # Test registering a user with an email that already exists
    response = test_client.post(
        '/register',
        json={
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'password'
        }
    )
    assert response.status_code == 400


def test_protected_route(test_client, new_user):
    # Test accessing protected route with valid JWT
    access_token = new_user.get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = test_client.get('/protected', headers=headers)
    assert response.status_code == 200


def test_protected_route_missing_jwt(test_client, new_user):
    # Test accessing protected route without JWT
    response = test_client.get('/protected')
    assert response.status_code == 401


def test_protected_route_invalid_jwt(test_client, new_user):
    # Test accessing protected route with invalid JWT
    headers = {
        'Authorization': 'Bearer invalid_token'
    }
    response = test_client.get('/protected', headers=headers)
    assert response.status_code == 401
