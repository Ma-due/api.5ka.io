from db import db
import uuid

class TeamModel(db.Model):
    __tablename__ = "teams"
    
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True,nullable=False)
    projects = db.relationship("ProjectModel", back_populates="teams", lazy="dynamic", cascade="all,delete")
    users = db.relationship("UserModel", back_populates="teams")
    