from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def getUsers():
    a = open("data/users.csv","r")
    list = a.readlines()
    dict = {}
    for user in list:
        entry = user.strip("\n").split(",")
        dict[entry[0]] = entry[1]
    a.close()
    return dict

def addUser(user, pw):
    a = open("data/users.csv","a")
    a.write(str(user)+","+str(pw)+"\n")
    a.close()
    return

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def authenticate():
    user = request.form["username"]
    pw = request.form["password"]
    dict = getUsers()
    shaHash = hashlib.sha1()
    shaHash.update(pw)
    pwHash = shaHash.hexdigest()
    if (user in dict):
        if (dict[user] == pwHash):
            return render_template("results.html", result="Login successful!")
    return render_template("results.html", result="Login failed!")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/regauth", methods=["POST"])
def regauth():
    user = request.form["username"]
    pw = request.form["password"]
    dict = getUsers()
    shaHash = hashlib.sha1()
    shaHash.update(pw)
    pwHash = shaHash.hexdigest()
    if (user in dict):
        return render_template("regresults.html", result="The username you entered is already taken. Go back to try again.")
    addUser(user,pwHash)
    return render_template("regsuccess.html")
    

if __name__=="__main__":
    app.debug = True #
    app.run()
