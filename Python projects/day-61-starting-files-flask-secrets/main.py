from flask import Flask, render_template
from wtforms import *
from flask_bootstrap import *
from wtforms.validators import *
import email_validator
from flask_wtf import FlaskForm

app = Flask(__name__)
app.secret_key = "prosecutable"
bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    email = EmailField("email", validators=[Email()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Login")


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
