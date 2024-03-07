from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user.splite3'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    roll = db.Column(db.String(50))
    subject = db.Column(db.String(50))
    contact = db.Column(db.String(50))
    
    def __init__(self,name,roll,subject,contact):
        self.name = name
        self.roll = roll
        self.subject = subject
        self.contact = contact
        
        
with app.app_context():
    db.create_all()        
    
    
student_list = [
    {"name": "Aarav", "roll": 101, "subject": "Mathematics", "contact": "5551234"},
    {"name": "Aditi", "roll": 102, "subject": "Physics", "contact": "5555678"},
    {"name": "sumit", "roll": 103, "subject": "Computer Science", "contact": "5559012"},
    {"name": "Rohan", "roll": 104, "subject": "Chemistry", "contact": "5553456"},
    {"name": "aman", "roll": 105, "subject": "Biology", "contact": "5557890"}
]    

@app.route("/upload")
def upload():
    for i in student_list:
        stud = Student(i["name"],i["roll"],i["subject"],i["contact"])
        db.session.add(stud)
    db.session.commit()
    return "success"

@app.route("/")
def home():    
    studentlist = Student.query.all()
    return render_template('home.html',data = studentlist)
    
    
    
    