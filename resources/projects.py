from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ProjectSchema, ProjectUpdateSchema
from db import db
from models import ProjectModel

blp = Blueprint("Projects", "projects", description="Operations on projects")

@blp.route("/project/<string:project_id>")
class Project(MethodView):
    @blp.response(200, ProjectSchema)
    def get(self, project_id):
        project = ProjectModel.query.get_or_404(project_id)
        return project

    def delete(self, project_id):
        project = ProjectModel.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        return {"message":"project deleted"}, 200
    
    @blp.arguments(ProjectUpdateSchema)
    # ProjectUpdateSchema에 정의된데로 데이터가 들어왔는지 확인
    @blp.response(200, ProjectSchema)
    # 요청에 대한 응답
    def put(self, project_data ,project_id):
        project = ProjectModel.query.get(project_id)
        if project:
            project.name = project_data["name"]
            project.type = project_data["type"]
            project.description = project_data["description"]
        else:
            project = ProjectModel(id=project_id, **project_data)
        
        db.session.add(project)
        db.session.commit()

        return project

@blp.route("/project")
class ProjectList(MethodView):
    @blp.response(200, ProjectSchema(many=True))
    def get(self):
        return ProjectModel.query.all()

    @blp.arguments(ProjectSchema)
    @blp.response(201, ProjectSchema)
    def post(self, project_data):
        project = ProjectModel(**project_data)

        try:
            db.session.add(project)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message = "An error occrred while inserting the project.")

        return project