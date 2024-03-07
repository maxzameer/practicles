from flask import Flask,url_for,render_template,request,redirect,flash,get_flashed_messages
import pandas as pd
import os



app = Flask(__name__)
app.secret_key = "heheh"
path = os.path.join("static","files")

print(path)



@app.route("/", methods=['GET', 'POST'])
def home(show = False,image = ""):
   
    flash("this is working") 
    return render_template("home.html",show=show,image = image)



@app.route("/upload", methods = ["post"])
def upoload():
    flash("this is working") 
    flash("this is working1")    
    flash("this is working2")
    file = request.files["file"]
    file.save(f"{path}\{file.filename}")
    return redirect("/")

@app.route("/table")
def tab():
    data = pd.read_csv("files/ford_escort.csv")   
    
    return render_template("table.html",table_html= data.to_html())
