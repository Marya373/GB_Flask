from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/1/")
def indexDZ():
    return render_template("indexDZ.html")


@app.route("/2/")
def clothDZ():
    return render_template("clothDZ.html")


@app.route("/3/")
def shuuzDZ():
    return render_template("shuuzDZ.html")


if __name__ == "__main__":
    app.run(debug=True)
