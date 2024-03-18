from flask import Flask,jsonify,request
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
        
    def to_json(self):
        return {
            "name": self.name,
            "roll": self.roll,
            "subject": self.subject,
            "contact": self.contact
        }    
        
        
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


@app.route("/create", methods=['POST'])
def create():
    
    data = request.get_json()
    
    name = data.get('name')
    roll = data.get('roll')
    subject = data.get('subject')
    contact = data.get('contact')
    
    if not name or not roll or not subject or not contact:
        return jsonify({"error": "Incomplete data provided"}), 400
    
    new_student = Student(name=name, roll=roll, subject=subject, contact=contact)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully"}), 200



@app.route("/read/<name>" ,methods = ['Get'])
def read(name):    
    student = Student.query.filter_by(name = name).first()
    print(student)
    return jsonify(student.to_json())


@app.route("/update/<name>", methods=['PUT'])
def update(name):
    student = Student.query.filter_by(name = name).first()
    if not student:
        return jsonify({"error": "Student not found"}), 404
    
    data = request.get_json()
    name = data.get('name')
    roll = data.get('roll')
    subject = data.get('subject')
    contact = data.get('contact')
    
    if name:
        student.name = name
    if roll:
        student.roll = roll
    if subject:
        student.subject = subject
    if contact:
        student.contact = contact
    
    db.session.commit()
    
    return jsonify({"message": "Student updated successfully"}), 200






@app.route("/delete/<name>", methods=['DELETE'])
def delete(name):
    student = Student.query.filter_by(name = name).first()
    if not student:
        return jsonify({"error": "Student not found"}), 404
    
    db.session.delete(student)
    db.session.commit()
    
    return jsonify({"message": "Student deleted successfully"}), 200
    
    
    
    