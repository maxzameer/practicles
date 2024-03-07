from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)

class Users(db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
        
        
with app.app_context():
    db.create_all()        



@app.route("/")
def home():
    return render_template("home.html")


@app.route('/process',methods=['post'])
def process():
    
    #create
    name = request.form['name']
    subject = request.form['subject']
    
    user = Users(name,subject)    
    db.session.add(user)
    
    db.session.commit()
    
    #read
    data = Users.query.all()
    for i in data:        
     print(i.name)  
     
    #update 
  #  data = Users.query.filter_by(name = "lohit").first()
  #  data.name = "mr lohit"
  #  db.session.commit()
    
     
    
    user = Users.query.filter_by(name = "mr lohit")
    user.delete()
    db.session.commit()
    
    #read
    data = Users.query.all()
    for i in data:        
     print(i.name)
    
   # data = Users.query.all()
   # for i in data:        
    # print(i.name)  
    
    
    
    return "hello"