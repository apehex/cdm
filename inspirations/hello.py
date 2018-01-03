from app import routes
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='ai')

@app.route('/')
def home():
    return render_template('home.html')
