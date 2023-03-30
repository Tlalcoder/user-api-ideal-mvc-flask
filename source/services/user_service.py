from source.models.user_model import db, User
from source.schemas.user_schema import UserSchema
from source.controllers import bcrypt


class UserService:
    @staticmethod
    def create_user(name, email, password):
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def update_password(user, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user.password = hashed_password
        db.session.commit()

    @staticmethod
    def check_password(user, password):
        return bcrypt.check_password_hash(user.password, password)

    @staticmethod
    def serialize_user(user):
        user_schema = UserSchema()
        return user_schema.dump(user)