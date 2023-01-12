import sqlite3 as sql
from pathlib import Path

from pydantic import BaseModel


DB_PATH = Path("guuber.db")
SQL_COMMANDS_PATH = Path(__file__).parent / "sql"


class Blog(BaseModel):
    ...

class SQLCommands:
    def __getattr__(self, name):
        path = SQL_COMMANDS_PATH / f"{name}.sql"
        return path.read_text()
sql_commands = SQLCommands()


def create_database():
    """Returns a database connection."""
    conn = sql.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.execute(sql_commands.create_blogs)
    return conn

        
    