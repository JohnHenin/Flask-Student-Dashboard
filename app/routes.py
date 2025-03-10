from flask import Blueprint, render_template
main = Blueprint("main", __name__)
@main.route("/")
def home():
    return render_template("index.html")
@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")