import sqlite3
from flask import *
from flask_sqlalchemy import *

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    # new_book=Book(id=1, title="Harry Potter", author="jk.rowling", rating=9.3)
    # db.session.add(new_book)
    # db.session.commit()
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
