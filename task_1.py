from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Word!"


@app.route("/about/")
def about():
    return "Gracias"


@app.route("/contact/")
def contact():
    return "Hoy"


if __name__ == "__main__":
    app.run(debug=True)
