from flask import Flask, jsonify
from flask_cors import CORS


import random

app = Flask(__name__)
CORS(app)

@app.route("/")
@app.route("/index")
def index():
    return "This is index"


@app.route("/hello_world")
def hello_world():
    return "Hello, World!"


@app.route("/hello_world_html")
def hello_world_html():
    return '<p style="color:tomato;">Hello, World!</p>'


@app.route("/some_json")
def some_json():

    weather = random.choice(["sunny", "rainy", "cloudy", "wet", "snowy"])

    return jsonify({
        "city_name": "London",
        "country_name": "United Kingdom",
        "population": 8000000,
        "weather": weather,
        "temperature": random.randint(20, 30),
        "wind_speed": random.randint(0, 10),
        "wind_direction": random.choice(["N", "S", "E", "W"])
    })


if __name__ == "__main__":
    app.run(debug=True)