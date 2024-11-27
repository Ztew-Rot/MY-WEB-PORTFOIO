from flask import session, request, render_template, Flask, url_for
from flask_session import Session
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///database.db")

@app.route("/")
def home():
    return render_template('home.html')

if (__name__)=="__main__":
    app.run(debug=True)

