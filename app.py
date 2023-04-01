from flask import Flask
from flask_jwt_extended import JWTManager
from source.config import Config
from source.models import db
from source.controllers import bcrypt
from source.controllers.user_controller import user_blueprint
from flask_restx import Api, Resource

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)


app.register_blueprint(user_blueprint, url_prefix='/user')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
