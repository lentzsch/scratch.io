from .db import db, environment, SCHEMA, add_prefix_for_prod
# from .users_games import users_games
# from .games_gamejams import games_gamejams
from .tags_games import tags_games

# from .users_games import User_Game

# ItemDetail = db.Table('games_gamejams',
#                       db.Column('id', db.Integer, primary_key=True),
#                       db.Column('gameId', db.Integer, db.ForeignKey('Item.id')),
#                       db.Column('gamejamId', db.Integer, db.ForeignKey('Detail.id')),
#                       db.column('gamePlacement'))

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    blurb = db.Column(db.Text)
    avatarUrl = db.Column(db.String(255))
    githubUrl = db.Column(db.String(255))
    websiteUrl = db.Column(db.String(255))
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    teamId = db.Column(db.Integer, db.ForeignKey('teams.id'))
    gameJamId = db.Column(db.Integer, db.ForeignKey('gamejams.id'))
    tags = db.relationship(
        "Tag",
        secondary=tags_games,
        back_populates="games"
    )

    def get_joined_tags(self):
        return [tag.to_dict() for tag in self.tags]

    # def get_joined_users(self):
    #     return [user.to_dict() for user in self.users]

    # def get_joined_gamejams(self):
    #     return [gamejam.to_dict() for gamejam in self.gamejams]

    def to_dict(self, tags=False):
        dct = {
            "id": self.id,
            "name": self.name,
            "blurb": self.blurb,
            "avatarUrl": self.avatarUrl,
            "githubUrl": self.githubUrl,
            "websiteUrl": self.websiteUrl,
            "userId": self.userId,
            "teamId": self.teamId,
            "gameJamId": self.gameJamId
        }

        if tags:
            dct["tags"] = self.get_joined_tags()

        return dct
        # if users:
        #     dct["users"] = self.get_joined_users()

        # if gamejams:
        #     dct["gamejams"] = self.get_joined_gamejams()


    # def to_dict_users(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "blurb": self.blurb,
    #         "avatarUrl": self.avatarUrl,
    #         "githubUrl": self.githubUrl,
    #         "websiteUrl": self.websiteUrl,
    #         "users": [user.to_dict() for user in self.users]
    #     }
