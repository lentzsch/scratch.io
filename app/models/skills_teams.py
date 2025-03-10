from .db import db, environment, SCHEMA, add_prefix_for_prod

skills_teams = db.Table(
    "skills_teams",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("teamId", db.Integer, db.ForeignKey(add_prefix_for_prod("teams.id"))),
    db.Column("skillId", db.Integer, db.ForeignKey(add_prefix_for_prod("skills.id")))
)

if environment == "production":
    skills_teams.schema = SCHEMA
