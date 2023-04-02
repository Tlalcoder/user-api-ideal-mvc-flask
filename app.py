from flask import Flask
from flask_jwt_extended import JWTManager
from source.config import Config
from source.models import db, migrate
from source.controllers import bcrypt
from source.blueprints import register_blueprints


# Create app
app = Flask(__name__)
# register config
app.config.from_object(Config)
# re
db.init_app(app)
# register bcrypt
bcrypt.init_app(app)
# register jwt
jwt = JWTManager(app)

migrate.init_app(app, db)

# Register blueprints
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
