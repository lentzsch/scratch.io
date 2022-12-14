from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.ext.declarative import declarative_base


teams_gamejams = db.Table(
    "teams_gamejams",
    db.Column('id', db.Integer, primary_key=True),
    db.Column("teamId", db.Integer, db.ForeignKey(add_prefix_for_prod("teams.id"))),
    db.Column("gameJamId", db.Integer, db.ForeignKey(add_prefix_for_prod("gamejams.id")))
)

if environment == "production":
    teams_gamejams.schema = SCHEMA
