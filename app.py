from flask import Flask, render_template
app = Flask(__name__)

import random

def dictionarify():
    #store the data from the csv into a list, s
    a = open ('occupations.csv', 'r')
    s = a.read()
    s = s.split('\n')
    #remove the titles and blank data
    s = s[1:len(s)-2]
    #make a dictionary
    dict = {}
    for job in s:
        #the Occupation is the string job up to the last comma, the percent is whats after the last comma
        if (job[0] == '"'):
            dict[job[1:job.rfind('"')]] = float(job[job.rfind(',')+1:])
        else:
            dict[job[:job.rfind(',')]] = float(job[job.rfind(',')+1:])
    return dict

def weightedrand(dict):
    r = random.random() * 99.8
    start = 0.0
    for job in dict:
        stop = start + dict[job]
        if (start <= r < stop):
            return job
        else:
            start = stop

def randjob():
    return weightedrand(dictionarify())


@app.route("/")
def hello_world():
    return "No hablo queso"


@app.route("/hi")
def hello():
    return "Ni Hao"


dict = dictionarify()
rand = randjob()

@app.route("/occupations")
def tablify():
    return render_template("basic.html", title="Occupations", data=dict, word=rand)

if __name__=="__main__":
    app.debug = True #
    app.run()
