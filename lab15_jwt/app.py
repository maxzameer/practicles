from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required,create_access_token,get_jwt_identity
app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "12345" 
jwt = JWTManager(app)

users = {"abc": {"password": "123"},
         "def": {"password": "456"}}




@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username]['password'] == password:
        
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
    
    

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
