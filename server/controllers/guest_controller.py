from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.guest import Guest
from server.models import db

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([
        {"id": guest.id, "name": guest.name, "occupation": guest.occupation}
        for guest in guests
    ])

# ✅ Add DELETE route here
@guest_bp.route('/guests/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_guest(id):
    guest = Guest.query.get(id)
    if not guest:
        return jsonify({"error": "Guest not found"}), 404

    db.session.delete(guest)
    db.session.commit()
    return jsonify({"message": "Guest deleted"}), 200
