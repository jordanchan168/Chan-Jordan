from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def authenticate():

    # DIAGNOSTICS
    #print "\n\n\n===DIAG=== this Flask obj"
    #print app
    #print "\n===DIAG=== this request obj"
    #print request
    #print "\n===DIAG=== this request headers obj"
    #print request.headers
    #print "\n===DIAG=== this request method obj"
    #print request.method
    #print "\n===DIAG=== this request form obj"

    if (request.form["username"]=="eublepharis" and request.form["password"]=="macularius"):
        return render_template("results.html", result="Login successful!")
    else:
        return render_template("results.html", result="Login failed!")


if __name__=="__main__":
    app.debug = True #
    app.run()
