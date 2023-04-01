# User API

This application implements a RESTful API to interact with a MySQL database and allow for user management.

## Usage

1. Clone the repository and navigate to the directory:
git clone https://github.com/Tlalcoder/user-api-ideal-mvc-flask.git
cd user-api-ideal-mvc-flask

markdown
Copy code

2. Install the required dependencies using the `requirements.txt` file:
pip install -r requirements.txt

markdown
Copy code

3. Run the application:
flask run

sql
Copy code

4. Navigate to `http://localhost:5000/api/users` to view the API documentation and available endpoints.

## Endpoints

The following endpoints are available:

- `GET /api/users`: get a list of all users
- `GET /api/users/<int:user_id>`: get a single user by ID
- `POST /api/users`: create a new user
- `PUT /api/users/<int:user_id>`: update an existing user
- `DELETE /api/users/<int:user_id>`: delete a user by ID

## Request and Response Formats

This API accepts and returns data in JSON format.