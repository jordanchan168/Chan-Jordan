from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
import utils.check
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)


@app.route("/")
def home():
    if ("username" in session):
        return redirect(url_for("logged_in"))
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def authenticate():
    user = request.form["username"]
    pw = request.form["password"]
    dict = utils.check.getUsers()
    shaHash = hashlib.sha1()
    shaHash.update(pw)
    pwHash = shaHash.hexdigest()
    if (user in dict):
        if (dict[user] == pwHash):
            session["username"] = user
            return redirect(url_for("logged_in"))
    return render_template("results.html", result="Login failed!")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/regauth", methods=["POST"])
def regauth():
    user = request.form["username"]
    pw = request.form["password"]
    dict = utils.check.getUsers()
    shaHash = hashlib.sha1()
    shaHash.update(pw)
    pwHash = shaHash.hexdigest()
    if (user in dict):
        return render_template("regresults.html", result="The username you entered is already taken. Go back to try again.")
    utils.check.addUser(user,pwHash)
    return render_template("regsuccess.html")


@app.route("/logged_in")
def logged_in():
    return render_template("logged_in.html", user=session["username"])


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("username")
    return redirect(url_for("home"))


if __name__=="__main__":
    app.debug = True #
    app.run()
