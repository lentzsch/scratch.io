from flask.cli import AppGroup
from .users import seed_users, undo_users
from .games import seed_games, undo_games
from .teams import seed_teams, undo_teams
from .skills import seed_skills, undo_skills
from .game_jams import seed_game_jams, undo_game_jams
from .tags import seed_tags, undo_tags
from .join_tables import seed_join_tables
from app.models.db import db, environment, SCHEMA


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding, truncate all tables prefixed with schema name
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
        # Add a truncate command here for every table that will be seeded.
        db.session.commit()
    seed_users()
    seed_teams()
    seed_game_jams()
    seed_games()
    seed_skills()
    seed_tags()
    seed_join_tables()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_games()
    undo_skills()
    undo_teams()
    undo_game_jams()
    undo_tags()
    # Add other undo functions here
