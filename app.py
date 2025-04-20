# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Wecome Home"

if __name__ == "__main__":
    app.run(debug = True)
