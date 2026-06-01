from datetime import datetime, timezone
from core.extensions import db
from sqlalchemy.dialects.postgresql import JSONB 


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password = db.Column(db.String(80), nullable=False, index=True)

