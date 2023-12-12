from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap4(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-library.db"
db.init_app(app)
KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZWM1YWNjYjczMmQxZTNhMGM4ZDdkNDVmNjk3ZDMyZiIsInN1YiI6IjY1Nzg2ZGQzN2EzYzUyMDBlYmZlNGZiOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.a_p7ZU_KMbnoX1uKOL17Jm5ImmiEXY95MVWSK8e4Rio"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)


try:
    with app.app_context():
        db.create_all()
except Exception as ex:
    print("Error Occurred ")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    movies = result.scalars()
    return render_template("index.html", movies=movies)


class EditForm(FlaskForm):
    rating = StringField("Your Rating", validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField("Done")


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    print(movie_id)
    if form.validate_on_submit():
        try:
            movie_to_update = db.get_or_404(Movie, movie_id)
            movie_to_update.rating = form.rating.data
            movie_to_update.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
        except Exception as ex:
            print("error occurred")

    return render_template("edit.html", form=form, movie_id=movie_id)


@app.route("/delete", methods=['GET', 'POSt'])
def delete():
    try:
        trash_movie = db.get_or_404(Movie, request.args.get('id'))
        db.session.delete(trash_movie)
        db.session.commit()
        return redirect(url_for('home'))
    except Exception as ex:
        print("Error Occurred")


class AddMovie(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Search")


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "query": movie_title
        }
        header = {
            "Authorization": f"Bearer {KEY}"
        }
        response = requests.get(url, headers=header, params=params)
        data = response.json()

        return render_template("select.html", movies=data)
    return render_template("add.html", form=form)


@app.route("/get_movie_details", methods=['GET', 'POST'])
def get_movie_details():
    movie_id = int(request.args.get('id'))
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    header = {
        "Authorization": f"Bearer {KEY}"
    }
    response = requests.get(url, headers=header)
    data = response.json()
    print(data)
    movie_update = Movie(title=data['title'],
                         year=data['release_date'],
                         description=data['overview'],
                         rating=0,
                         ranking=10,
                         review="No review",
                         img_url=f"https://image.tmdb.org/t/p/original{data['backdrop_path']}")
    try:
        db.session.add(movie_update)
        db.session.commit()
    except Exception as ex:
        print("error occured")
    return redirect(url_for('edit', id=movie_update.id))


if __name__ == '__main__':
    app.run(debug=True)
