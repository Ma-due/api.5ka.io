from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from passlib.hash import pbkdf2_sha256
from db import db
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import UserModel
from schemas import UserSchema, UserLoginSchema
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)
from blocklist import BLOCKLIST


blp = Blueprint("users", __name__, description="Operations on teams")

@blp.route("/join")
class UserJoin(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.user_id == user_data["user_id"]).first():
            abort(409, message="A user with that username already exists.")
        
        user = UserModel(
            user_id = user_data["user_id"],
            name = user_data["name"],
            password = pbkdf2_sha256.hash(user_data["password"]),
            email = user_data["email"],
            team_id = user_data["team_id"]
        )

        db.session.add(user)
        db.session.commit()
        return {"message":"User Created succesfully"}, 201

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserLoginSchema)
#    @blp.response(201, UserLoginSchema)
    def post(self, login_data):
        user = UserModel.query.filter(
            UserModel.user_id == login_data["user_id"]
        ).first()

        if user and pbkdf2_sha256.verify(login_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200

        abort(401, message="Invalid credentials.")

@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200