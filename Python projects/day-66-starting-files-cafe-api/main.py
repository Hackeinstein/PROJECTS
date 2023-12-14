from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# to dict
def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# get random record
@app.route("/random", methods=['GET'])
def get():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    cafe = random.choice(all_cafes)
    return jsonify(cafe=to_dict(cafe))


# get all records
@app.route("/all", methods=['GET'])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafe=[to_dict(cafe) for cafe in all_cafes])


# search for records
@app.route("/search", methods=['GET'])
def search_cafe():
    location = request.args.get("loc")
    try:
        result = db.session.execute(db.select(Cafe).filter_by(location=location))
        all_cafes = result.scalars().all()
        if all_cafes:
            return jsonify(cafe=[to_dict(cafe) for cafe in all_cafes])
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    except Exception as ex:
        print(ex)
        return jsonify(
            error={
                "Not Found": "Sorry, we don't have a cafe at that location"
            }
        )



@app.route("/add", methods=["GET","POST"])
def add_cafe():
    new_cafe=Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),

    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe. "})



# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
