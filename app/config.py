import os
class Config:
    SECRET_KEY = os.urandom(5)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://luisg:Sk81398@localhost:5432/db_tatto'
    SQLALCHEMY_TRACK_MODIFICATIONS = False