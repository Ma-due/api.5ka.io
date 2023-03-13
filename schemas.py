from marshmallow import Schema, fields

class PlainProjectSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    description = fields.Str(required=True)

class PlainTeamSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ProjectSchema(PlainProjectSchema):
    team_id = fields.Str(required=True)
    team = fields.Nested(PlainTeamSchema(), dump_only=True)

class ProjectUpdateSchema(Schema):
    name = fields.Str()
    type = fields.Str()
    description = fields.Str()

class TeamSchema(PlainTeamSchema):
    projects = fields.List(fields.Nested(PlainProjectSchema()), dump_only=True)