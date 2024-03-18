from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from faker import Faker

app = Flask(__name__)
fake = Faker('en_IN')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False


db = SQLAlchemy(app)

class User(db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
  
    
    def __init__(self,name):
        self.name = name
        
        
with app.app_context():
    db.create_all()   


@app.route("/<int:num>")
def home(num):
    print(num)
    
    data = User.query.paginate(per_page=5,page=num)
    
    
    print(data.pages)
    
    return render_template("home.html",data = data)

@app.route("/signin")
def signin(): 
       
    for i in range(100):      

        user = User(fake.name())
        db.session.add(user)
    db.session.commit()
    
    data = User.query.all()
    for i in range(10):
     print(data[i].name)     
    
    return "successful"
    
    