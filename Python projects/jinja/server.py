from flask import Flask, render_template
import random
import requests

app = Flask(__name__)


@app.route("/<_name>")
def home(_name):
    query1 = requests.get("https://api.genderize.io", params={
        "name": _name
    })
    _gender = query1.json()['gender']
    query2 = requests.get("https://api.agify.io", params={
        "name": _name
    })
    _age = query2.json()['age']
    return render_template("index.html",
                           name=_name, age=_age, gender=_gender)


@app.route("/blog")
def blog():
    query = requests.get("https://api.npoint.io/b08185f2bb1d5693ca69")
    blog_post=query.json()
    return render_template("blog.html", posts=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
