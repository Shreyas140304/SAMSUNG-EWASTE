from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql%402025@localhost/ewaste_management"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'

db = SQLAlchemy()