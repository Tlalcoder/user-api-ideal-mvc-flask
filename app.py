from flask import Flask
from flask_jwt_extended import JWTManager
from source.config import Config
from source.models import db
from source.controllers import bcrypt
from source.controllers.user_controller import user_blueprint
from source.controllers.root_controller import root_blueprint

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

# Register blueprints
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(root_blueprint)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
