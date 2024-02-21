from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/demo")
def xyz():
    return "Hello world"
        

