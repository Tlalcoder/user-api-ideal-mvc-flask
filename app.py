from flask import Flask
from flask_jwt_extended import JWTManager
from source.config import Config
from source.models import db
from source.controllers import bcrypt, api
from source.controllers.user_controller import user_blueprint

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
# register swagger
api.init_app(app)

# Register blueprints
app.register_blueprint(user_blueprint, url_prefix='/user')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
