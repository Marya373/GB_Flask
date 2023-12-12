from flask import Flask

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Мария</h1>
<p>Я учусь и в голове уже каша</p>
"""


@app.route("/")
def index():
    return "Hi!"


@app.route("/text/")
def text():
    return html


@app.route("/poems/")
def poems():
    poem = ["Заметает, зима, заметает"]
    txt = "<h1>Стихотворение</h><p>" + "<br/>".join(poem) + "</p>"
    return txt


if __name__ == "__main__":
    app.run(debug=True)
