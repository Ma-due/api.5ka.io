from marshmallow import Schema, fields

class ProjectSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str(required=True)
    description = fields.Str(required=True)
    team_id = fields.Str(required=True)

class ProjectUpdateSchema(Schema):
    name = fields.Str()
    type = fields.Str()
    description = fields.Str()

class TeamSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)