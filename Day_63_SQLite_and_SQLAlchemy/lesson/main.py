# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter and the Deathly Hallows', 'J. K. Rowling', '9.3')")

# db.commit()

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy()

# Initialize the app with the extension
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f'<Book {self.title}'
    
#Create table schema in the database.  Requires application context.
with app.app_context():
    db.create_all()

# ## CREATE RECORD
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter and the Deathly Hallows", author="J.K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

# Read All Records 
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()

print(all_books)


# # Read a particular record by Query
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter and the Deathly Hallows")).scalar()

