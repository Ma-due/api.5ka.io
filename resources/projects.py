import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import projects
from schemas import ProjectSchema, ProjectUpdateSchema

blp = Blueprint("Projects", "projects", description="Operations on projects")

@blp.route("/project/<string:project_id>")
class Project(MethodView):
    @blp.response(200, ProjectSchema)
    def get(self, project_id):
        try:
            return projects[project_id]
        except KeyError:
            abort(404,messaeg="Projct not found")

    def delete(self, project_id):
        try:
            del projects[project_id]
            return {"message": "Project deleted."}
        except KeyError:
            abort(404, message="Project not found")
    
    @blp.arguments(ProjectUpdateSchema)
    # ProjectUpdateSchema에 정의된데로 데이터가 들어왔는지 확인
    @blp.response(200, ProjectSchema)
    # 요청에 대한 응답
    def put(self, project_data ,project_id):
        try:
            project = projects[project_id]
            project |= project_data
            return project

        except KeyError:
            abort(404, message="Project not found")

@blp.route("/project")
class ProjectList(MethodView):
    @blp.response(200, ProjectSchema(many=True))
    def get(self):
        return projects.values()

    @blp.arguments(ProjectSchema)
    @blp.response(201, ProjectSchema)
    def post(self, project_data):
        for project in projects.values():
            if(
                project_data["name"] == project["name"]
                and project_data["project_id"] == project["project_id"]
            ):
                abort(400, message="project alreadt exists")

        project_id = uuid.uuid4().hex
        project = {"id": project_id, **project_data}
        projects[project_id] = project

        return project