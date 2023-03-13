from db import db
import uuid

class ProjectModel(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True,nullable=False)
    type = db.Column(db.String(30),unique=False,nullable=False)
    description = db.Column(db.String(200),unique=False,nullable=False)
    # projects 테이블에서 teams.id 컬럼을 FK로 사용한다.
    team_id = db.Column(db.String(36), db.ForeignKey("teams.id"), unique=False,nullable=False)
    teams = db.relationship("TeamModel", back_populates="projects")
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False, unique=False)
    users = db.relationship("UserModel", back_populates="projects")