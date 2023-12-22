from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    query = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = query.json()
    return render_template("index.html", posts=posts)


@app.route("/post/<int:_id>")
def post(_id):
    blog = None
    query = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = query.json()
    for post in posts:
        if post['id'] == _id:
            title=post['title']
            body=post['body']
    return render_template("post.html", title=title,body=body)


if __name__ == "__main__":
    app.run(debug=True)
