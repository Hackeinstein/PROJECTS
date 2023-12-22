from flask import Flask, render_template, request
import requests

app = Flask(__name__)

feed = ""


@app.route("/")
def home():
    query = requests.get("https://api.npoint.io/330b90acdf98d0ccc75c")
    posts = query.json()
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['number'])
        print(request.form['message'])
        return "<h1> Submitted successfully</h1>"
    else:
        return render_template("contact.html")


@app.route("/post/<index>")
def post(index: int):
    global feed
    query = requests.get("https://api.npoint.io/330b90acdf98d0ccc75c")
    posts = query.json()
    for _post in posts:
        print(_post)
        print(index)
        print(_post["id"])
        if int(index) == int(_post["id"]):
            feed = _post
    return render_template("post.html", feed=feed)


# @app.route("/form-entry", methods=['POST'])
# def receive_data():



if __name__ == "__main__":
    app.run(debug=True)
