from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap4(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)
# CKEDITOR
ckeditor = CKEditor(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).filter_by(id=post_id)).scalar()
    return render_template("post.html", post=requested_post)


# Declearing form for new post
class BlogForm(FlaskForm):
    title = StringField("Blog Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    url = StringField("Image Url", validators=[DataRequired()])
    body = CKEditorField("Body")
    submit = SubmitField("Add Post")


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=['POST', 'GET'])
def new_post():
    time = dt.datetime.now()
    form = BlogForm()
    if form.validate_on_submit():
        try:
            new_data = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                author=form.author.data,
                img_url=form.url.data,
                body=form.body.data,
                date=time.strftime("%B %d, %Y")
            )
            db.session.add(new_data)
            db.session.commit()
            return redirect(url_for("show_post", post_id=new_data.id))
        except Exception as ex:
            print(ex)
    return render_template("make-post.html", form=form, new="New Post")


# TODO: edit_post() to change an existing blog post
@app.route("/edit/post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    form = BlogForm(
        title=post.title,
        subtitle=post.subtitle,
        url=post.img_url,
        author=post.author,
        body=post.body
    )
    if form.validate_on_submit():
        try:
            post.title = form.title.data
            post.subtitle = form.subtitle.data
            post.author = form.author.data
            post.img_url = form.url.data
            post.body = form.body.data
            db.session.commit()
            return redirect(url_for("show_post", post_id=post.id))
        except Exception as ex:
            print(ex)

    return render_template("make-post.html", new="Edit Post", form=form, post=post)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/post/<int:post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    except Exception as ex:
        print(ex)


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
