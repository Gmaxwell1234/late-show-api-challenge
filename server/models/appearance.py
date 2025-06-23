from . import db


class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))

    guest = db.relationship("Guest", back_populates="appearances")
    episode = db.relationship("Episode", back_populates="appearances")

    def __repr__(self):
        return f"<Appearance Guest={self.guest_id} Episode={self.episode_id} Rating={self.rating}>"
