from flask import Flask
from flask import render_template

app = Flask(__name__)


# this is decorator
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # main()
    # flask automatically start development, when files changed in project
    app.run(debug=True)

# add in the README.md about resources used:
# 1. bootstrap CSS
