from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/index/")
def html_table():
    context = [
        {"name": "Jane",
         "last_name": "Danes",
         "age": "25"},
        {"name": "Mary",
         "last_name": "Faiv",
         "age": "35"},
        {"name": "Ksenya",
         "last_name": "Chist",
         "age": "35"},
    ]
    return render_template("table.html", context=context)


if __name__ == "__main__":
    app.run(debug=True)
