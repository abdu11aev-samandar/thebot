from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def register():
    return render_template("register.html")


@app.route('/register_check', methods=["GET", "POST"])
def register_check():
    age = request.form.get("age")
    age_int=int(age)
    if age >= 20:
        return render_template("success.html")
    else:
        return render_template("error.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/error")
def error():
    return render_template("error.html")


app.run(debug=True)
