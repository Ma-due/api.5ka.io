from db import db

class TeamModel(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True,nullable=False)
    projects = db.relationship("ProjectModel", back_populates="team", lazy="dynamic", cascade="all,delete")
    