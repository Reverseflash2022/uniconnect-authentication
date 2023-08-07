from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    _hashed_password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    courses = db.Column(db.String(500))  # This can be improved with a proper relationship later

    def __repr__(self):
        return f"<Student {self.username}>"

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self._hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._hashed_password, password)

