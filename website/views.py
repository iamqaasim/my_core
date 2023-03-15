# Blueprint is used to sort our routes
# Render_template is used to render the html pages
from flask import Blueprint, render_template, jsonify

# Define blueprint named views
views = Blueprint('views',__name__)


# Create routes
# Create Home route
@views.route('/')
def home():
  return render_template("home.html")

@views.route('/mind')
def mind():
  return render_template("mind.html")

@views.route('/body')
def body():
  return render_template("body.html")

@views.route('/soul')
def soul():
  return render_template("soul.html")

@views.route('/finance')
def finance():
  return render_template("finance.html")

@views.route('/network')
def network():
  return render_template("network.html")

@views.route('/ai_tools')
def ai_tools():
  return render_template("ai_tools.html")
