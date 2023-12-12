from flask import *
import sqlite3
from flask_sqlalchemy import *

# create database and catch error if it exists
# try:
#     _db = sqlite3.connect("library.db")
# except Exception as ex:
#     print("Database already exists")

# flask and sql config variables
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
db.init_app(app)

all_books = []


# table structure
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# create table and catch error if table exists
try:
    with app.app_context():
        db.create_all()
except Exception as ex:
    print("table already exists")


@app.route('/')
def home():
    global all_books
    try:
        results = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = results.scalars()
    except Exception as ex:
        print("Error occured")
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    global all_books
    if request.method == "POST":
        try:
            new_book = Books(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
            db.session.add(new_book)
            db.session.commit()
        except Exception as ex:
            print(f"Error occurred \n{ex}")
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Books, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Books, book_id)
    return render_template("edit.html", book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)
