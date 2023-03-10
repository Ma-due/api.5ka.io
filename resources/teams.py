import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import teams
from schemas import TeamSchema

blp = Blueprint("teams", __name__, description="Operations on teams")

@blp.route("/team/<string:team_id>")
class Team(MethodView):
    @blp.response(200, TeamSchema)
    def get(self, team_id):
        try:
            return teams[team_id]
        except KeyError:
            abort(404, message = "Team not found")

    def delete(self, team_id):
        try:
            del teams[team_id]
            return {"message":"Team deleted"}
        except KeyError:
            abort(404,message="Team not found")

@blp.route("/team")
class TeamList(MethodView):
    @blp.response(200, TeamSchema(many=True))
    def get(self):
      return list(teams.values())

    @blp.arguments(TeamSchema)
    @blp.response(201, TeamSchema)
    def post(self, team_data):
        for team in teams.values():
            if team_data["name"] == team["name"]:
                abort(400, message="Team alreadt exists")

        team_id = uuid.uuid4().hex
        team = {"id":team_id, **team_data}
        teams[team_id] = team

        return team