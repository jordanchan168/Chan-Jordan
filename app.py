from flask import Flask, render_template
from utils import jobs

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso"


@app.route("/hi")
def hello():
    return "Ni Hao"


@app.route("/occupations")
def tablify():
    return render_template("basic.html", title="Occupations", data=jobs.dictionarify(), word=jobs.randjob())

if __name__=="__main__":
    app.debug = True #
    app.run()
