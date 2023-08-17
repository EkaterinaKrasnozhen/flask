import os
import random

from flask import Flask, render_template
from task2.models import db, Author, Book, BookAuthor

app = Flask(__name__)
app.secret_key =b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///books.db'
db.init_app(app)


@app.route('/')
def index():
    return "hello"


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route("/books/")
def get_books():
    all_books = Book.query.all()
    context = {'books': all_books}
    return render_template("books.html", **context)


if __name__ == "__main__":
    app.run(debug=True)