from server.models import db
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    serialize_rules = ("-password_hash",)

    @property
    def password_hash(self):
        raise AttributeError("Password is write-only.")

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = generate_password_hash(password).decode('utf-8')

    def authenticate(self, password):
        return check_password_hash(self._password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"
