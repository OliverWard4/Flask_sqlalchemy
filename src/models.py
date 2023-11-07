# TODO - Create SQLAlchemy DB and Movie model

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ItemModel(db.Model):
    __tablename__ = "movie"  

    movie_id = db.Column(db.Integer, primary_key=True)  # change the collums names to the ones mentioned in movies sql file
    title = db.Column(db.String(80), unique=True, nullable=False)
    director = db.Column(db.Float(precision=2), unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)