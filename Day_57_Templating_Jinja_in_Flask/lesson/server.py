from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    today = datetime.date.today()
    current_year = today.year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender = gender_response.json()["gender"]
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template('blog.html', posts=blog_data)



if __name__ == "__main__":
    app.run(debug=True)


