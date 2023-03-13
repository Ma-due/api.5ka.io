from marshmallow import Schema, fields

class PlainUserSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)


class PlainProjectSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    description = fields.Str(required=True)

class PlainTeamSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class UserSchema(PlainUserSchema):
    team_id = fields.Str(required=True)
    team = fields.Nested(PlainTeamSchema(), dump_only=True)
    projects = fields.List(fields.Nested(PlainProjectSchema()), dump_only=True)

class UserLoginSchema(Schema):
    user_id = fields.Str(required=True)
    password = fields.Str(required=True)

class ProjectSchema(PlainProjectSchema):
    team_id = fields.Str(required=True)
    team = fields.Nested(PlainTeamSchema(), dump_only=True)
    user_id = fields.Str(required=True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)

class ProjectUpdateSchema(Schema):
    name = fields.Str()
    type = fields.Str()
    description = fields.Str()

class TeamSchema(PlainTeamSchema):
    projects = fields.List(fields.Nested(PlainProjectSchema()), dump_only=True)
    user = fields.List(fields.Nested(PlainUserSchema()), dump_only=True)