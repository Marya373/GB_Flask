from flask import Flask

app = Flask(__name__)


@app.route("/<name>/")
def hello(name="незнакомец"):
    return f"Привет, {name.capitalize()}!"

if __name__ == "__main__":
    app.run(debug=True)
