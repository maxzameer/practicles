from flask import Flask,jsonify,request
# pip install mysql-connector-python
import mysql.connector


app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Students"
)

cursor = db.cursor()

        
        
    
    
student_list = [
    {"name": "Aarav", "roll": 101, "subject": "Mathematics"},
    {"name": "Aditi", "roll": 102, "subject": "Physics"},
    {"name": "sumit", "roll": 103, "subject": "Computer Science"},
    {"name": "Rohan", "roll": 104, "subject": "Chemistry"},
    {"name": "aman", "roll": 105, "subject": "Biology"}
]    

@app.route("/upload")
def upload():
    sql = "INSERT INTO person (roll,name, subject) VALUES (%s, %s,%s)"
    for i in student_list:
        
        val = (i["roll"],i["name"],i["subject"])
        cursor.execute(sql, val)
        db.commit()
    return "success"

@app.route("/readall")
def read_records():
    cursor.execute("SELECT * FROM person")
    records = cursor.fetchall()
    d = {}
    for record in records:
        d.update({ record[0] : record})
        
    return jsonify(data = d)   


@app.route("/create", methods=['POST'])
def create():    
    data = request.get_json()    
    name = data.get('name')
    roll = data.get('roll')
    subject = data.get('subject')
    
    sql = "INSERT INTO person (roll,name, subject) VALUES (%s, %s,%s)"
    val = (roll ,name, subject)
    cursor.execute(sql, val)
    db.commit()
    return jsonify({"message": "Student added successfully"}), 200



@app.route("/read/<name>" ,methods = ['Get'])
def read(name):    
    
    sql = "SELECT * FROM person WHERE name = %s"
    val = (name,)
    cursor.execute(sql, val)
    record = cursor.fetchone()
    if record:
        print(record)
    else:
        print("No record found with id:", name)
    return jsonify(record)    
    
 
   


@app.route("/update/<name>", methods=['PUT'])
def update(name):
    
    
    data = request.get_json()
    new_name = data.get('name')
    roll = data.get('roll')
    subject = data.get('subject')
    
    sql = "UPDATE person SET name = %s, roll = %s,subject = %s WHERE name = %s"
    val = (new_name, roll,subject, name)
    cursor.execute(sql, val)
    db.commit()    
    return jsonify({"message": "Student updated successfully"}), 200






@app.route("/delete/<name>", methods=['DELETE'])
def delete(name):
    sql = "DELETE FROM person WHERE name = %s"
    val = (name,)
    cursor.execute(sql, val)
    db.commit()    
    return jsonify({"message": "Student deleted successfully"}), 200
    
    
    
    