from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.models import db, User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 409

    user = User(username=username)
    user.password_hash = password

    db.session.add(user)
    db.session.commit()

    token = create_access_token(identity=user.id)
    return jsonify({"message": "User registered", "token": token}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.authenticate(password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)
    return jsonify({"message": "Login successful", "token": token}), 200
