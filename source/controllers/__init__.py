from flask_bcrypt import Bcrypt
from flask_restx import Api

api = Api(version='1.0', title='User API', description='API for managing users')
bcrypt = Bcrypt()


