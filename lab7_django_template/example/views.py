from django.shortcuts import render
from django.http import HttpResponse

student_list = [
    {"name": "Aarav", "roll": 101, "subject": "Mathematics", "contact": "5551234"},
    {"name": "Aditi", "roll": 102, "subject": "Physics", "contact": "5555678"},
    {"name": "sumit", "roll": 103, "subject": "Computer Science", "contact": "5559012"},
    {"name": "Rohan", "roll": 104, "subject": "Chemistry", "contact": "5553456"},
    {"name": "aman", "roll": 105, "subject": "Biology", "contact": "5557890"}
] 

# Create your views here.

def home(response):
    return render(response,"home.html",{"data":student_list})

#@app.route("/")
#def home():
 #   return "hello"