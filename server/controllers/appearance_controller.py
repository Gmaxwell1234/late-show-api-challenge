# server/controllers/appearance_controller.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required  # ← add this
from server.models.appearance import Appearance
from server.models import db

appearance_bp = Blueprint('appearance', __name__, url_prefix='/appearances')

@appearance_bp.route('', methods=['POST'])
@jwt_required()  # ← protect creation
def create_appearance():
    data = request.get_json()
    try:
        ap = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(ap)
        db.session.commit()
        return jsonify({
            "id": ap.id,
            "rating": ap.rating,
            "guest_id": ap.guest_id,
            "episode_id": ap.episode_id
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 400
