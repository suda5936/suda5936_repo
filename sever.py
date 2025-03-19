from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://10.0.2.2:5000"])

app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)
users = mongo.db.users

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    if users.find_one({"email": email}):
        return jsonify({"error": "이미 존재하는 이메일입니다."}), 400
    
    hashed_password = generate_password_hash(password)
    users.insert_one({"email": email, "password": hashed_password})
    
    return jsonify({"message": "회원가입 성공!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    user = users.find_one({"email": email})
    
    if user and check_password_hash(user["password"], password):
        return jsonify({"message": "로그인 성공!"}), 200
    else:
        return jsonify({"error": "이메일 또는 비밀번호가 잘못되었습니다."}), 400

if __name__ == '__main__':
    app.run(host="10.0.2.2", port=5000, debug=True)
