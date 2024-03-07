from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False


db = SQLAlchemy(app)

class User(db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
with app.app_context():
    db.create_all()   


@app.route("/")
def home():
    
    return render_template("home.html")

@app.route("/signin",methods = ["post"])
def signin():
    name= request.form["name"]
    email = request.form["email"]
    user = User(name,email)
    db.session.add(user)
    db.session.commit()
    
    data = User.query.filter_by(name="abc").first()
    print(data.name)
    print(data.email)   
    
    data2 = User.query.filter_by(name="abc").first()
    data2.name = "parth"
    db.session.commit()
    
    data1 = User.query.filter_by(name="parth")
    data1.delete()
    db.session.commit()
    
    data1 = User.query.all()
    for i in data1:
        print(i.name)
        

      
    
    return "successful"
    
    