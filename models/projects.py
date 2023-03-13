from db import db

class ProjectModel(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80), unique=True,nullable=False)
    type = db.Column(db.String(30),unique=False,nullable=False)
    description = db.Column(db.String(200),unique=False,nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), unique=False,nullable=False)
    team = db.relationship("TeamModel", back_populates="projects")