from flask import Flask,jsonify,request
# pip install pymongo
#  
import pymongo


app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["School"]  # Choose or create database
collection = db["students"]  # Choose  or create collection



        
        
    
    
student_list = [
    {"name": "Aarav", "roll": 101, "subject": "Mathematics"},
    {"name": "Aditi", "roll": 102, "subject": "Physics"},
    {"name": "sumit", "roll": 103, "subject": "Computer Science"},
    {"name": "Rohan", "roll": 104, "subject": "Chemistry"},
    {"name": "aman", "roll": 105, "subject": "Biology"}
]    

@app.route("/upload")
def upload():
    collection.insert_many(student_list)  
    return "success"


@app.route("/readall")
def read_records():
    
    records = collection.find()
    print(records)    
    d = {}
    for record in records:
        del record["_id"]
        d.update({ record["name"] : record})        
    return jsonify(data = d)   


@app.route("/create", methods=['POST'])
def create():    
    data = request.get_json()    
    name = data.get('name')
    roll = data.get('roll')
    subject = data.get('subject')
    
    data = {"name": name, "roll": roll, "subject": subject}
    collection.insert_one(data)
    return jsonify({"message": "Student added successfully"}), 200



@app.route("/read/<name>" ,methods = ['Get'])
def read(name):    
    
    record = collection.find_one({"name": name})
    del record["_id"]
    return jsonify(record)    
    
 
   


@app.route("/update/<name>", methods=['PUT'])
def update(name):
    
    
    data = request.get_json()
    new_name = data.get('name')
    roll = data.get('roll')
    subject = data.get('subject')
    
    collection.update_one({"name": name}, {"$set": {"name": new_name, "roll": roll, "subject": subject}})


    updated_result = collection.find_one({"name": new_name})
    
    print(updated_result) 
    return jsonify({"message": "Student updated successfully"}), 200






@app.route("/delete/<name>", methods=['DELETE'])
def delete(name):
    collection.delete_one({"name": name})    
    return jsonify({"message": "Student deleted successfully"}), 200


    
    
    
    