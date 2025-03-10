from .db import db, environment, SCHEMA, add_prefix_for_prod


skills_users = db.Table(
    "skills_users",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("userId", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id"))),
    db.Column("skillId", db.Integer, db.ForeignKey(add_prefix_for_prod("skills.id")))
)

if environment == "production":
    skills_users.schema = SCHEMA

# db.Column('id', db.Integer, primary_key=True),
#     db.Column("userId", db.Integer, db.ForeignKey("users.id")),
#     db.Column("gameId", db.Integer, db.ForeignKey("games.id"))
