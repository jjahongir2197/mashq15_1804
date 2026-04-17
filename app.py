from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def password_match():

    if request.method == "POST":

        p1 = request.form["p1"]
        p2 = request.form["p2"]

        if p1 == p2:
            return "Parollar mos"

        else:
            return "Parollar mos emas"

    return render_template("index.html")

app.run(debug=True)
