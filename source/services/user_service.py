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
    def get_user_by_id(user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    @staticmethod
    def get_all_users():
        users = User.query.all()
        return users

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

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True
