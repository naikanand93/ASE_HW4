from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/save")
def saveData():
    return "Hello World!"


