from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def main()->str:
    return "<h1>Guess a number from 0-9</h1><br><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

no=random.randint(0,10)
print(no)
@app.route("/<number>")
def guess(number)->str:
    if int(number) > no:
        return "<h1>To High try again</h1><br><img src='https://media.giphy.com/media/3QWfMsI8IaarXxtBt6/giphy.gif'>"
    elif int(number) < no:
        return "<h1>To Low try again</h1><br><img src='https://media.giphy.com/media/iJJ6E58EttmFqgLo96/giphy.gif'>"
    elif int(number) == no:
        return "<h1 style='color:green'>You found me!</h1><br><img src='https://media.giphy.com/media/t3sZxY5zS5B0z5zMIz/giphy.gif'>"


@app.route("/bye/<name>")
def bye(name)->str:
    """ bye function """
    return f"<h1>Bye {name}</h1>"



if __name__ == "__main__":
    app.run()
