from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

@app.route("/")
def hello_world():
    return render_template("index.html")

# @app.route("/forms/contact.php", methods = ["POST", "GET"])
# def contact_form():
#     return render_template("forms/contact.php")

if __name__ == "__main__":
    app.run(debug = True)