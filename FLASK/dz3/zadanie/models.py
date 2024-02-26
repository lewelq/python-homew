from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String, nullable = False)
    name = db.Column(db.String, nullable = False)
    surname = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)

    