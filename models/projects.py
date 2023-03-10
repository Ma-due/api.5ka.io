from db import db

class ProjectModel(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Cloumn(db.String(80), unique=True,nullable=False)
    type = db.Cloumn(db.String(30),unique=False,nullable=False)
    description = db.Cloumn(db.String(200),unique=False,nullable=False)
    team_id = db.Cloumn(db.Integer, db.ForeginKey("teams.id"), unique=False,nullable=False)
    team = db.relationship("TeamModel", back_populates="teams")