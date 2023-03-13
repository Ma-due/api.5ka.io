from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import TeamModel
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import TeamSchema

blp = Blueprint("teams", __name__, description="Operations on teams")

@blp.route("/team/<string:team_id>")
class Team(MethodView):
    @blp.response(200, TeamSchema)
    def get(self, team_id):
        team = TeamModel.query.get_or_404(team_id)
        return team

    def delete(self, team_id):
        team = TeamModel.query.get_or_404(team_id)
        db.session.delete(team)
        db.session.commit()
        return {"message":"team deleted."}

@blp.route("/team")
class TeamList(MethodView):
    @blp.response(200, TeamSchema(many=True))
    def get(self):
      return TeamModel.query.all()

    @blp.arguments(TeamSchema)
    @blp.response(201, TeamSchema)
    def post(self, team_data):
        team = TeamModel(**team_data)
        try:
            db.session.add(team)
            db.session.commit()
        # unique = true 여서 기존 data가 있으면 에러
        except IntegrityError:
            abort(400, message="A Team with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occured creating the Team")
        return team