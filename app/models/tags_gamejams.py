from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.ext.declarative import declarative_base


tags_gamejams = db.Table(
    "tags_gamejams",
    db.Column("tagId", db.Integer, db.ForeignKey(add_prefix_for_prod("tags.id"))),
    db.Column("gameJamId", db.Integer, db.ForeignKey(add_prefix_for_prod("gamejams.id")))
)

if environment == "production":
    tags_gamejams.schema = SCHEMA