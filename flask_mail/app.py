from flask import Flask 
from flask_mail import Mail, Message 
   
app = Flask(__name__) 
mail = Mail(app) 
   
# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 
 
@app.route("/") 
def home(): 
   msg = Message( 
                'Hello', 
                sender ='yourId@gmail.com', 
                recipients = ['receiver’sid@gmail.com'] 
               ) 
   msg.body = 'Hello Flask message sent from Flask-Mail'
   Message()
   mail.send(msg) 
   return 'Sent'

# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PEJQSmQNZZhblu3rF215dhXWitTUJ6BS2Ov2TT7rJ7c4cMjiZvNiwVVgSa2nAvg6oL8eiaKkQSbJPqaCoEu0FGhHfM-A68StEBJoTR4fOejQvPa8o