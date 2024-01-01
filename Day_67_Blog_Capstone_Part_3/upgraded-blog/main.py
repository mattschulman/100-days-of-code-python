from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# Create the Form Structure to be able to create/edit a post
class NewPostForm(FlaskForm):
    title = StringField(label='Blog Title', validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    img_url = StringField(label='Blog Image URL', validators=[DataRequired(), URL()])
    # the body field uses CKEditor
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = []
    #Get all records from the DB, then convert to a list to send to the index.html page for rendering
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Fetch the post record from the DB and render the page with the data.
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=["GET", "POST"])
def make_post():
  # Create a post form to send to the page to be rendered.
  form = NewPostForm()  
  if form.validate_on_submit():
       # Create a new DB record with information submitted in the form, commit to the DB, and return to the home page.
       new_post = BlogPost(
           title = form.title.data,
           subtitle = form.subtitle.data,
           body = form.body.data,
           img_url = form.img_url.data,
           author = form.author.data,
           date = date.today().strftime("%B %d, %Y")
       )
       db.session.add(new_post)
       db.session.commit()
       return redirect(url_for("get_all_posts"))
  return render_template("make-post.html", form=form)


@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    # Fetch the post record from the DB
    post = db.get_or_404(BlogPost, post_id)
    #Inside the form, fill in the existing data
    edit_form = NewPostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    #Update the information from the submitted form, and update the DB record.  Return to the post page
    if edit_form.validate_on_submit():
        post.title=edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.body = edit_form.body.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)



@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)