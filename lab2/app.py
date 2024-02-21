from flask import Flask,render_template,request,redirect

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        
data = {}        

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/reg",methods=["post"])
def reg():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    user = User(name,email,password)
    data.update({email:user})    
    return redirect("/login")

@app.route("/signin",methods=["post"])
def signin():   
    email = request.form["email"]
    password = request.form["password"]
    
    if email in data:
        user = data[email]
        if password == user.password:
            return render_template("user.html",message ="login success")
        else:
            return render_template("user.html",message = "you have entered a wrong password")
    
    else:
        return render_template("user.html",message ="please enter a valid email address") 
        



        
