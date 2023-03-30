import os
from dotenv import load_dotenv
load_dotenv()
print(os.environ.get('DATABASE_URL'))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret-key'