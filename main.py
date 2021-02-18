from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hei! Yo! Ai!</h1>"

@app.route("/json")
def json():
    f = open("dati.json", "r", encoding="utf-8")
    return f.read()

if __name__ == '__main__':
    app.run(debug=True)