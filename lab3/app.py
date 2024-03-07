from flask import Flask,render_template,request,send_file

app = Flask(__name__)
l = []
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/downloadpage")
def downloadpage():
    return render_template("downloadpage.html",data=l)

@app.route("/upload",methods=["post"])
def upload():
    file = request.files["file"]
    name = request.form["name"]
    ext = file.filename[-4:]
    filename = name + ext
    l.append(filename)    
    file.save(f"files/{filename}")       
    return filename

@app.route("/getdata",methods=["post"])
def xyz():
    name = request.form['name']          
    return send_file(f"files/{name}") 

@app.errorhandler(404)
def error(e):
    print(type(e))
    return "error",404



