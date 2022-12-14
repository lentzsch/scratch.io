from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.ext.declarative import declarative_base


tags_games = db.Table(
    "tags_games",
    db.Column("tagId", db.Integer, db.ForeignKey("tags.id")),
    db.Column("gameId", db.Integer, db.ForeignKey("games.id"))
)
