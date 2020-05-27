from flask import Blueprint, render_template, jsonify

main_route = Blueprint("route", __name__)

@main_route.route("/")
def index():
    return render_template("")