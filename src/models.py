# TODO - Create SQLAlchemy DB and Movie model

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = "movie"  

    movie_id = db.Column(db.Integer, primary_key=True)  # change the collums names to the ones mentioned in movies sql file
    title = db.Column(db.String(255), unique=True, nullable=False)
    director = db.Column(db.String(255), unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, title: str, director: str, rating: int) -> None:
        self.title = title
        self.director = director
        self.rating = rating

    def __repr__(self) -> str:
        return f'Movie (title = {self.title})'