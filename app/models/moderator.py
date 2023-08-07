from app import db

class Moderator(db.Model):
    __tablename__ = "moderators"

    id = db.Column(db.Integer, primary_key=True)
    moderator_id = db.Column(db.String(80), unique=True, nullable=False)
    associated_university = db.Column(db.String(250), nullable=False)
    permissions = db.Column(db.String(500))  # This can be improved with a proper permissioning system later

