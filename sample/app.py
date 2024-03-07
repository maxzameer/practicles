from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    
    
    def __init__(self,name,subject,contact):
        self.name = name
        self.subject = subject
        self.contact = contact
        

with app.app_context():
    db.create_all()        
        
              
def process():
    data = [{'name' : "zameer",
             'subject' : 'java',
             'contact': '123456'},
            {'name' : "goku",
             'subject' : 'MartialArt',
             'contact': '1251564'},
            {'name' : "Gohan",
             'subject' : 'Litrature',
             'contact': '5461664'},
            {'name' : "Picallo",
             'subject' : 'MartialArt',
             'contact': '26492555'}]
    
    for i in data:
        stu = Student(i["name"],i["subject"],i["contact"])
        db.session.add(stu)
        
    db.session.commit()
    
    
   
    
@app.route('/')
def home():
    
   # process()
    data = Student.query.all()
    print(data)
    return render_template("home.html",students = data )
    
        
    
   
            