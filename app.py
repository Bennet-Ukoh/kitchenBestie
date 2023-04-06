from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    response = requests.get("https://api.spoonacular.com/recipes/search?apiKey=1948934612124d9e920b0dcbfe7078f0&number=1&query=" + q)
    data = response.json()
    return jsonify(data)

@app.route("/landingpage")
def landingpage():
    return render_template("landingpage.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/favorites")
def favorites():
    return render_template("favorites.html")
    





if __name__ == '__main__':
    app.run(debug=True)
