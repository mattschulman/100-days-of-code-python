from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import requests
import os

TMDB_API_TOKEN=os.environ.get("TMDB_TOKEN")
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"#

class EditForm(FlaskForm):
    rating = StringField(label='Your Rating (ie 7.5 out of 10)')
    review = StringField(label='Your Review')
    submit = SubmitField(label="Done")

class AddForm(FlaskForm):
    title = StringField(label="Movie Title")
    submit = SubmitField(label="Add Movie")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

## CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Create the Extension
db = SQLAlchemy()
# Initialize the app with the extension
db.init_app(app)

## CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(1024), nullable=True)
    img_url=db.Column(db.String(250), nullable=False)

#Create table schema in the DB.  Requires app context
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    ## READ ALL RECORDS
    # Construct a query to select from the database.  Returns the rows in the database. Order by the rating field
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() # convert ScalarResult to Python List

    #Set the ranking field for each movie based on the rating field
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()

    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit_movie():
    form = EditForm() 
    #Retrieve the index of the movie to be edited, get the row, and update the row
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id) 
    if form.validate_on_submit():
        if form.rating.data:
            movie.rating=float(form.rating.data)
        if form.review.data:
            movie.review=form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete_movie():
    #Retreieve the index of the movie to be deleted, get the row, and delete it
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form=AddForm()
    
    if form.validate_on_submit():
        movie_title = form.title.data
        #Search TMDB for movies that match the title input into the form
        tmdb_url = f"{MOVIE_DB_SEARCH_URL}?query={movie_title}&include_adult=false&language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_TOKEN}"
        }

        response = requests.get(tmdb_url, headers=headers)
        data=response.json()["results"]
        #Send the data to the webpage for rendering the movie titles and release dates
        return render_template('select.html', options=data)
    return render_template('add.html', form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        #The TMDB Movie ID of the selected Movie will be used to Query TMDB to get the movie details
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}?language=en-US"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_TOKEN}"
        }
        response = requests.get(movie_api_url, headers=headers)
        data = response.json()
        #Construct a new DB row using title, year, img_url, and description from the data returned from TMDB
        new_movie = Movie(
            title = data["title"],
            #The data in realse_date includes month and day, we will want to strip it
            year = data["release_date"].split('-')[0],
            img_url = f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description = data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
