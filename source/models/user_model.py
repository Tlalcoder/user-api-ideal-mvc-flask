from . import db
from datetime import datetime
from source.controllers import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, name, email, password, last_name, created_at, updated_at):
        self.name = name
        self.email = email
        self.last_name = last_name
        self.created_at = created_at
        self.updated_at = updated_at
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
