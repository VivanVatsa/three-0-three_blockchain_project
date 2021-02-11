from flask import Flask
from flask import render_template
from flask import request
from block import write_block, check_integrity

app = Flask(__name__)


# this is decorator
@app.route("/", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        borrower = request.form.get("borrower")
        lender = request.form.get("lender")
        amount = request.form.get("amount")

        write_block(borrower=borrower, lender=lender, amount=amount)
        # to check the working:
        # print(borrower)
        # print(lender)
        # print(amount)
    return render_template("index.html")


if __name__ == "__main__":
    # main()
    # flask automatically start development, when files changed in project
    app.run(debug=True)

# add in the README.md about resources used:
# 1. bootstrap CSS
