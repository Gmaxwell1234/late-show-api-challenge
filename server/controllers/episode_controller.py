# server/controllers/episode_controller.py

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required  # ← add this
from server.models.episode import Episode
from server.models import db

episode_bp = Blueprint('episode', __name__, url_prefix='/episodes')

@episode_bp.route('', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {"id": ep.id, "date": ep.date, "number": ep.number}
        for ep in episodes
    ])

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [
            {
                "id": ap.id,
                "rating": ap.rating,
                "guest_id": ap.guest_id
            } for ap in episode.appearances
        ]
    })

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()  # ← protect delete
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message=f"Deleted episode {id}"), 200
