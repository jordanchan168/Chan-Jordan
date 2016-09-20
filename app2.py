from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
<span style="font-family:Monospace">

SNAKE: <br>
&nbsp;&nbsp;   Y<br>
&nbsp;  / \<br>
&nbsp;  \ /<br>
&nbsp;  | |<br>
&nbsp;  \ \<br>
&nbsp;&nbsp;   \ \<br>
&nbsp;&nbsp;   | |<br>
&nbsp;&nbsp;   / /<br>
&nbsp;  / /<br>
&nbsp;  | |<br>
&nbsp;  \ \<br>
&nbsp;&nbsp;   \/<br>
&nbsp;&nbsp;   ()<br>
&nbsp;&nbsp;    ()<br>
&nbsp;&nbsp;     ()<br>

</span>

'''

@app.route("/home")
def hello_jordan():
    return '''
<span style="font-family:Monospace">

SNAKE: <br>
&nbsp;&nbsp;   Y<br>
&nbsp;  / \<br>
&nbsp;  \ /<br>
&nbsp;  | |<br>
&nbsp;  \ \<br>
&nbsp;&nbsp;   \ \<br>
&nbsp;&nbsp;   | |<br>
&nbsp;&nbsp;   / /<br>
&nbsp;  / /<br>
&nbsp;  | |<br>
&nbsp;  \ \<br>
&nbsp;&nbsp;   \/<br>
&nbsp;&nbsp;   ()<br>
&nbsp;&nbsp;    ()<br>
&nbsp;&nbsp;     ()<br>

</span>

'''

@app.route("/snake")
def ahello_jordan():
    return '''
<span style="font-family:Monospace">

SNAKE: <br>
&nbsp;&nbsp;   Y<br>
&nbsp;  / \<br>
&nbsp;  \ /<br>
&nbsp;  | |<br>
&nbsp;  \ \<br>
&nbsp;&nbsp;   \ \<br>
&nbsp;&nbsp;   | |<br>
&nbsp;&nbsp;   / /<br>
&nbsp;  / /<br>
&nbsp;  | |<br>
&nbsp;  \ \<br>
&nbsp;&nbsp;   \/<br>
&nbsp;&nbsp;   ()<br>
&nbsp;&nbsp;    ()<br>
&nbsp;&nbsp;     ()<br>

</span>

'''

if __name__== "__main__":
    app.run()
